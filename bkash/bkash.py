import datetime
import random
from typing import Literal

import requests
from django.conf import settings
from rest_framework.exceptions import APIException

from .models import (PaymentReference, PaymentReferenceStatusChoices,
                     RequestLog, ResponseLog)

INTENT_CHOICES = Literal['sale', 'authorization']


class PaymentCreateBody:
    mode: str
    payer_reference: str
    callback_url: str
    agreement_id: str
    amount: str
    currency: str
    intent: str
    merchant_invoice_number: str

    def __init__(self,
                 payer_reference: str,
                 amount: str,
                 merchant_invoice_number: str = None,
                 agreement_id: str = 'str',
                 callback_url: str = settings.BKASH_CALLBACK_URL,
                 currency: str = "BDT",
                 intent: str = "sale",
                 mode: str = "0011",
                 ):
        self.mode = mode
        self.payer_reference = payer_reference
        self.callback_url = callback_url
        self.agreement_id = agreement_id
        self.amount = amount
        self.currency = currency
        self.intent = intent
        self.merchant_invoice_number = merchant_invoice_number or self.generate_merchant_invoice_number(
            prefix="DJASH",
            length=10
        )

    def generate_merchant_invoice_number(self, prefix, length):
        return f"{prefix}"+datetime.datetime.now().strftime("%y%m%d%H%M%S") + \
            str(random.randint(10, 99))

    def to_dict(self):
        return {
            "mode": self.mode,
            "payerReference": self.payer_reference,
            "callbackURL": self.callback_url,
            "agreementID": self.agreement_id,
            "amount": self.amount,
            "currency": self.currency,
            "intent": self.intent,
            "merchantInvoiceNumber": self.merchant_invoice_number,
        }


class TokenizedCheckout:
    _APP_KEY = settings.BKASH_APP_KEY
    _APP_SECRET = settings.BKASH_APP_SECRET
    _USERNAME = settings.BKASH_USERNAME
    _PASSWORD = settings.BKASH_PASSWORD
    _BASE_URL = settings.BKASH_BASE_URL
    _TOKENIZED_GRANT_URL_ENDPOINT = '/tokenized/checkout/token/grant'
    _TOKENIZED_CREATE_PAYMENT_URL_ENDPOINT = '/tokenized/checkout/create'
    _TOKENIZED_EXECUTE_PAYMENT_URL_ENDPOINT = '/tokenized/checkout/execute'
    __access_token = None
    payment_url = None
    payer_reference = None  # payer reference on execution

    def __init__(self):
        if not self.__access_token:
            self._authenticate()

    def _raise_api_exception(self, response):
        raise APIException({
            "code": response.get('statusCode'),
            "message": response.get('statusMessage')
        })

    def _dispatch(self, endpoint, body={}, headers={}, method="POST", auth=True):
        url = self._BASE_URL + endpoint
        request = requests.Session()
        if auth:
            request.headers.update({
                "Authorization": self.__access_token,
                'x-app-key': self._APP_KEY
            })
        request.headers.update(headers)
        RequestLog.objects.create(
            url=url,
            method=method,
            headers=request.headers,
            body=body
        )
        response = request.request(
            method=method,
            url=url,
            json=body
        )
        ResponseLog.objects.create(
            status_code=response.status_code,
            headers=response.headers,
            body=response.json()
        )
        if response.status_code in range(200, 300):
            response_body = response.json()
            if response_body.get('statusCode') == '0000':
                return response_body
            else:
                self._raise_api_exception(response_body)

    def _authenticate(self):
        result = self._dispatch(
            endpoint=self._TOKENIZED_GRANT_URL_ENDPOINT,
            body={
                "app_key": self._APP_KEY,
                "app_secret": self._APP_SECRET
            },
            headers={
                "username": self._USERNAME,
                "password": self._PASSWORD
            },
            auth=False
        )
        self.__access_token = f"{result.get('token_type')} {result.get('id_token')}"

    def create_payment_url(self,
                           payment_options: PaymentCreateBody
                           ):
        payment_reference = PaymentReference(
            payer_reference=payment_options.payer_reference,
            merchant_invoice_number=payment_options.merchant_invoice_number
        )
        result = self._dispatch(
            endpoint=self._TOKENIZED_CREATE_PAYMENT_URL_ENDPOINT,
            body=payment_options.to_dict(),
            method="POST"
        )
        payment_reference.payment_id = result.get('paymentID')
        payment_reference.save()
        self.payment_url = result.get('bkashURL')
        self.payer_reference = payment_options.payer_reference
        return result

    def execute_payment(self, payment_id):
        data = {
            "paymentID": payment_id
        }
        payment_reference = PaymentReference.objects.get(
            payment_id=payment_id
        )
        self.payer_reference = payment_reference.payer_reference
        result = self._dispatch(
            endpoint=self._TOKENIZED_EXECUTE_PAYMENT_URL_ENDPOINT,
            body=data,
        )
        if not payment_reference.status == PaymentReferenceStatusChoices.COMPLETED:
            payment_reference.status = result.get('transactionStatus')
        payment_reference.save()
        return result

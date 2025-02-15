import os
from typing import List

import requests
from celery import shared_task
from django.core.mail import EmailMessage, send_mass_mail
from django.db import models
from django.template import Context, Template
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from genericpath import exists
from rest_framework import viewsets

from .models import (EmailContent, NewsLetter, StatusEmail, StatusSMS,
                     Subscriber)
from .serializers import NewsLetterSerializer, SubscriberSerializer


# Create your views here.
class SubscriberViewset(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer


class NewsLetterViewset(viewsets.ModelViewSet):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer


def send_submitted_email(applications=None):
    if applications:
        SUBJECT = "Your primary application has been successfully submitted!"
        for applicant in applications:
            html_content = render_to_string(template_name='newsletter/submitted.html', context={
                                            'ID': applicant.id, 'NAME': applicant.name, 'EMAIL': applicant.email})
            email = EmailMessage(
                SUBJECT,
                strip_tags(html_content),
                'noreply@joinarmyiba.com',
                [applicant.email]
            )
            email.attach_file('newsletter/images/' +
                              'Army IBA Application Steps - ApplyKoro.Com.png')
            email.send(fail_silently=True)


def send_awaiting_payment_email(applicants=None):
    if applicants:
        SUBJECT = "Congratulations! You've been elected to take the Army IBA entrance exam!"
        email_recipients = []
        for applicant in applicants:
            html_content = render_to_string(template_name='newsletter/approved.html', context={
                                            'ID': applicant['id'], 'NAME': applicant['name'], 'EMAIL': applicant['email']})
            email = EmailMessage(
                SUBJECT,
                strip_tags(html_content),
                'noreply@joinarmyiba.com',
                [applicant['email']]
            )
            email.attach_file(
                'newsletter/images/Nagad x Army IBA Payment Process - App Format - ApplyKoro.Com.png')
            email.attach_file(
                'newsletter/images/' + 'Nagad x Army IBA Payment Process - Manual SMS Format - ApplyKoro.Com.png')
            email_recipients.append(email)
            email.send(fail_silently=True)
        # send_mass_mail(email_recipients, fail_silently=False)


def send_status_change_email(applications: List = [], status: str = None):
    if applications:
        if status:
            if StatusEmail.objects.filter(status=status, active=True).exists():
                status_email = StatusEmail.objects.filter(
                    status=status, active=True).first()
                SUBJECT = status_email.subject
                SENDER = status_email.mail_from
                try:
                    TEMPLATE = status_email.template.path
                except:
                    TEMPLATE = None
                for application in applications:
                    if TEMPLATE:
                        html_content = render_to_string(TEMPLATE, context={
                            'ID': application.id,
                            'NAME': application.name,
                            'VENUE': application.venue,
                            'EMAIL': application.email})
                        body = strip_tags(html_content)
                    else:
                        body = Template(status_email.body)
                        body = body.render(
                            Context({'ID': application.id,
                                    'NAME': application.name,
                                     'EMAIL': application.email}))

                    email = EmailMessage(
                        SUBJECT,
                        body,
                        SENDER,
                        [application.email]
                    )
                    for attachment in status_email.attachments.all():

                        email.attach_file(attachment.file.path)
                    email.send(fail_silently=True)


@shared_task
def send_sms(mobile: str = None, body: str = None):
    if mobile and body:
        data = {'api_key': os.getenv('SMS_API_KEY'),
                'api_secret': os.getenv('SMS_API_SECRET'),
                "request_type": "SINGLE_SMS",
                'message_type': "UNICODE",
                "mobile": mobile,
                "message_body": body,
                }
        res = requests.post(
            'https://portal.adnsms.com/api/v1/secure/send-sms', data=data)


def send_status_change_sms(applications: List = [], status: str = None, **kwargs):
    countdown = kwargs.get('countdown', 1)
    if applications:
        if status:
            status_sms = StatusSMS.objects.filter(
                status=status, active=True).first()
            if status_sms:
                for application in applications:
                    body = Template(status_sms.body)
                    body = body.render(
                        Context({'ID': application.id,
                                'NAME': application.name,
                                'PHONE': application.phone,
                                'VENUE': application.venue,
                                }))
                    try:
                        send_sms.apply_async(
                            args=(application.phone, body), countdown=countdown)
                    except Exception as e:
                        print(e)
                    # data = {'api_key': os.getenv('SMS_API_KEY'),
                    #         'api_secret': os.getenv('SMS_API_SECRET'),
                    #         "request_type": "SINGLE_SMS",
                    #         'message_type': "UNICODE",
                    #         "mobile": application.phone,
                    #         "message_body": body,
                    #         }


def send_payment_reminder_sms(applications: List = [], status: str = None, to_guardian=False):

    if applications:
        if status:
            if StatusSMS.objects.filter(status=status, active=True).exists():
                status_sms = StatusSMS.objects.filter(
                    status=status, active=True).first()
                sms = {}
                for index, application in enumerate(applications):
                    body = Template(status_sms.body)
                    body = body.render(
                        Context({'ID': application.id,
                                'NAME': application.name}))
                    sms[f'sms[{index}][mobile]'] = application.guardians_phone if to_guardian is True else application.phone
                    sms[f'sms[{index}][message_body]'] = body
                data = {'api_key': os.getenv('SMS_API_KEY'),
                        'api_secret': os.getenv('SMS_API_SECRET'),
                        "request_type": "MULTIBODY_CAMPAIGN",
                        'message_type': "UNICODE",
                        "campaign_title": "Army IBA Payment Reminder",
                        }
                data.update(sms)
                r = requests.post(
                    'https://portal.adnsms.com/api/v1/secure/send-sms', data=data)
                if r.status_code == 200:
                    return True
                else:
                    raise Exception(r.text)

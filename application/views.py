
from typing import Any

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from rest_framework import parsers, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from analytics.models import ApplicantWorkingExperience, ApplicationNewsSource
from bkash.bkash import *

from .admit_card import generate_admit_card
from .models import (ApplicantExtraInformation, Application,
                     ApplicationPayment, ApplicationStatus)
from .serializers import (ApplicantExtraInformationSerializer,
                          ApplicationPaymentSerializer, ApplicationSerializer,
                          ApplicationStatusSerializer)


class SeatPlanListView(ListView):
    queryset = ApplicantExtraInformation.objects.all()
    context_object_name = 'applicants'
    template_name: str = 'application/seat_plan.html'
    model = ApplicantExtraInformation

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        if self.request.GET.get('venue'):
            queryset = queryset.filter(
                application__venue__icontains=self.request.GET.get('venue')).order_by('serial')
        return queryset


class DhakaApplicationView(ListView):
    queryset = ApplicantExtraInformation.objects.filter(
        application__venue='Dhaka').order_by('serial')
    context_object_name = 'applicants'
    template_name: str = 'application/dhaka_seat.html'
    paginate_by = 50
    model = ApplicantExtraInformation
# class ApplicationCreationView(CreateView):
#     model = Application
#     fields = "__all__"

#     # def post(self, request, *args, **kwargs):
#     #     return super().post(request, *args, **kwargs)


class ApplicationStatusViewset(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ApplicationStatus.objects.all()
    serializer_class = ApplicationStatusSerializer

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = ApplicationStatus.objects.get(
                application_id=kwargs['pk'])
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except:
            return Response({'message': 'Application Not Found'}, status=status.HTTP_404_NOT_FOUND)


class ApplicationViewset(ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()

    @action(detail=False, methods=['get'], url_path='find',)
    def find_application(self, request, pk=None):
        try:
            application = Application.objects.get(phone=request.GET.get('phone'), date_of_birth=request.GET.get('date_of_birth')
                                                  )
            serializer = ApplicationSerializer(application)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Application not found"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['get'], url_path='download',)
    def download_admit(self, request, pk=None):
        try:
            application = Application.objects.get(
                id=request.GET.get('application_id'), applicationstatus__status='photo_submitted')
            if application:
                admit_card_file = generate_admit_card(application)
                return FileResponse(open(admit_card_file, 'rb'), as_attachment=True, filename='admit_card.pdf')
        except ObjectDoesNotExist:
            return Response({"message": "Application not found"}, status=status.HTTP_404_NOT_FOUND)


class ApplicationPaymentViewset(ModelViewSet):
    serializer_class = ApplicationPaymentSerializer
    queryset = ApplicationPayment.objects.all()
    BKASH_TRANSACTION_AMOUNT = 1000

    def create(self, request, *args, **kwargs):
        application_id = request.data.get('application')
        serializer = self.get_serializer(
            data={'application': application_id, 'transaction_id': request.data.get('transaction_id')})
        serializer.is_valid(raise_exception=True)
        return super().create(request, *args, **kwargs)

    @action(methods=['get'], url_path='find', detail=False)
    def find_payment(self, request, pk=None):
        application_id = request.GET.get('application_id')

        try:
            payment = ApplicationPayment.objects.get(
                application__id=application_id)
            if payment:
                if ApplicantExtraInformation.objects.filter(application=payment.application).exists():
                    return Response({"message": "Application already has extra information"}, status=status.HTTP_400_BAD_REQUEST)
                if payment.verified:
                    if payment.application.applicationstatus.status == 'payment_completed':
                        serializer = self.get_serializer(payment)
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response({
                            "message":
                            "We have verified your payment. Please wait till we approve it."},
                            status=status.HTTP_400_BAD_REQUEST)
                elif payment.verified is False:
                    return Response({"message": "Payment could not be verified."}, status=status.HTTP_400_OK)
                else:
                    return Response({
                        "message": "Your payment information has been submitted.We need to verify your payment before proceeding to the next step."
                    },
                        status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "We could not find any payment associated with your application ID. Please complete payment first."}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['post'], url_path='bkash/create', detail=False)
    def bkash_payment_create(self, request, pk=None):
        application = request.data.get('application')
        serializer = self.get_serializer(
            data={'application': application})
        serializer.validate_application(application)
        tokenized_checkout = TokenizedCheckout()
        tokenized_checkout.create_payment_url(
            PaymentCreateBody(
                amount=self.BKASH_TRANSACTION_AMOUNT,
                payer_reference=application,
            )
        )
        return Response({
            "payment_url": tokenized_checkout.payment_url,
        })

    @action(methods=['post'], url_path='bkash/execute', detail=False)
    def bkash_payment_execute(self, request, pk=None):
        payment_id = request.data.get('payment_id')
        tokenized_checkout = TokenizedCheckout()
        tokenized_checkout.execute_payment(payment_id)
        application = Application.objects.get(
            id=tokenized_checkout.payer_reference
        )
        application_payment = ApplicationPayment.objects.create(
            application=application,
            transaction_id=payment_id,
            verified=True
        )
        application.applicationstatus.status = 'payment_completed'
        application.applicationstatus.save()
        return Response({
            "message": "Payment completed successfully",
            "payment": ApplicationPaymentSerializer(application_payment).data
        })


class ApplicantExtraInformationViewset(ModelViewSet):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    serializer_class = ApplicantExtraInformationSerializer
    queryset = ApplicantExtraInformation.objects.all()

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        application_info = super().create(request, *args, **kwargs)
        news_source = {
            'information_source': request.data.get('information_source'),
            'information_source_details': request.data.get(
                'information_source_details'
            )if
            request.data.get(
                'information_source_details'
            ) else
            None,
        }
        ApplicationNewsSource.objects.create(
            application_info_id=application_info.data['id'], **news_source)
        experience_details = {
            'has_working_experience': request.data.get('has_working_experience'),
            'working_experience_details': request.data.get('working_experience_details'),
        }
        ApplicantWorkingExperience.objects.create(
            application_info_id=application_info.data['id'], ** experience_details)
        return application_info

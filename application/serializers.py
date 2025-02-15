from django.db.models import Q
from rest_framework import serializers

from globals import CURRENT_BATCH

from .models import (ApplicantExtraInformation, Application,
                     ApplicationPayment, ApplicationStatus)


class ApplicationStatusSerializer(serializers.ModelSerializer):
    status_text = serializers.ReadOnlyField(source='get_status_display')
    payment_verified = serializers.ReadOnlyField(
        source='application.applicationpayment.verified')

    class Meta:
        model = ApplicationStatus
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    batch = serializers.CharField(
        default=CURRENT_BATCH
    )

    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['id']
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('phone', 'date_of_birth', 'batch'),
                message=("You have already registered."))

        ]
        # exclude = ['is_approved']


class ApplicationPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationPayment
        fields = '__all__'

    def validate_application(self, value):
        application = Application.objects.filter(id=value).first()
        if not application:
            raise serializers.ValidationError(
                "Application not found")
        if application:
            existing_payment = ApplicationPayment.objects.filter(
                application=application).first()
            if existing_payment and existing_payment.verified:
                raise serializers.ValidationError(
                    "You have already paid for this application and Payment is verified")
            elif existing_payment and not existing_payment.verified:
                raise serializers.ValidationError(
                    "Your payment information has been submitted. You'll get a confirmation email once we verify your payment.")
            elif not existing_payment and not (application.applicationstatus.status in ['awaiting_payment', 'awaiting_payment_reminder',
                                                                                        'payment_not_received']):
                raise serializers.ValidationError(
                    "You can not submit your payment now. Wait for application to be approved.")
        return value


class ApplicantExtraInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicantExtraInformation
        fields = '__all__'

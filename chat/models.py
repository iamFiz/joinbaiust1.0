from django.core.exceptions import ValidationError
from django.db import models

from application.models import CurrentBatchMeta, TimeDateMixin
from globals import BATCH_CHOICES, CURRENT_BATCH

# Create your models here.

CHAT_RESPONSE_CHOICES = (('responded', 'Responded'),
                         ('not_responded', 'Not Responded'))
CHAT_REQUEST_PROBLEM_TYPE = (
    ('website', 'Website'),
    ('during_application', 'During Application'),
    ('circular', 'Circular'),
    ('payment', 'Payment'),
    ('photo_upload', 'Photo Upload'),
    ('open_payment_window', 'Open Payment Window'),
    ('others', 'Others'),
)


class ChatRequest(TimeDateMixin, CurrentBatchMeta):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()
    area = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(
        choices=CHAT_RESPONSE_CHOICES, max_length=25, default='not_responded')
    application_id = models.CharField(max_length=255, null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    response_via = models.CharField(max_length=255, null=True, blank=True, choices=(
        ('email', 'Email'), ('phone', 'Phone'), ('sms', 'SMS'), ('whatsapp', 'WhatsApp'), ('other', 'Other')))
    problem_type = models.CharField(
        max_length=255, null=True, blank=True, choices=CHAT_REQUEST_PROBLEM_TYPE, )

    response_via_other = models.CharField(
        max_length=255, null=True, blank=True)

    batch = models.CharField(
        default=CURRENT_BATCH,
        choices=BATCH_CHOICES, max_length=25)

    def clean(self) -> None:
        if self.response_via == 'other':
            if not self.response_via_other:
                raise ValidationError(
                    'Please specify the response method')
        return super().clean()

    class Meta:
        verbose_name_plural = 'Chat Requests'


class SMSRequest(TimeDateMixin, CurrentBatchMeta):
    assigned_to = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    problem = models.TextField()
    problem_type = models.CharField(
        max_length=255, null=True, blank=True, choices=CHAT_REQUEST_PROBLEM_TYPE, )
    responded = models.BooleanField(default=False)
    application_id = models.CharField(max_length=255, null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    response_via = models.CharField(max_length=255, null=True, blank=True, choices=(
        ('email', 'Email'), ('phone', 'Phone'), ('sms', 'SMS'), ('whatsapp', 'WhatsApp'), ('other', 'Other')))
    response_via_other = models.CharField(
        max_length=255, null=True, blank=True)

    batch = models.CharField(
        default=CURRENT_BATCH,
        choices=BATCH_CHOICES, max_length=25)

    class Meta:
        verbose_name_plural = 'SMS Requests - Internal'

    def clean(self) -> None:
        if self.response_via == 'other':
            if not self.response_via_other:
                raise ValidationError(
                    'Please specify the response method')
        return super().clean()


class PhoneRequest(TimeDateMixin, CurrentBatchMeta):
    assigned_to = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    problem = models.TextField()
    problem_type = models.CharField(
        max_length=255, null=True, blank=True, choices=CHAT_REQUEST_PROBLEM_TYPE, )
    responded = models.BooleanField(default=False)
    application_id = models.CharField(max_length=255, null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    response_via = models.CharField(max_length=255, null=True, blank=True, choices=(
        ('email', 'Email'), ('phone', 'Phone'), ('sms', 'SMS'), ('whatsapp', 'WhatsApp'), ('other', 'Other')))
    response_via_other = models.CharField(
        max_length=255, null=True, blank=True)
    batch = models.CharField(
        default=CURRENT_BATCH,
        choices=BATCH_CHOICES, max_length=25)

    class Meta:
        verbose_name_plural = 'Phone Requests - Internal'

    def clean(self) -> None:
        if self.response_via == 'other':
            if not self.response_via_other:
                raise ValidationError(
                    'Please specify the response method')
        return super().clean()

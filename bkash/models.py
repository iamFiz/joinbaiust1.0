from django.db import models


class PaymentReferenceStatusChoices(models.TextChoices):
    INITIATED = ('Initiated', 'Initiated')
    PENDING = ('Pending', 'Pending')
    COMPLETED = ('Completed', 'Completed')
    FAILED = ('Failed', 'Failed')
    CANCELLED = ('Cancelled', 'Cancelled')


class MetaFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PaymentReference(MetaFields):
    payer_reference = models.CharField(max_length=50, editable=False)
    merchant_invoice_number = models.CharField(
        max_length=50, editable=False, unique=True)
    payment_id = models.CharField(
        max_length=50, editable=False, unique=True)
    status = models.CharField(
        max_length=20, choices=PaymentReferenceStatusChoices.choices, default=PaymentReferenceStatusChoices.INITIATED)

    def __str__(self):
        return self.payer_reference+'-'+self.merchant_invoice_number

    class Meta:
        verbose_name_plural = "Payment References"
        verbose_name = "Payment Reference"
        ordering = ['-created_at']


class RequestLog(MetaFields):
    url = models.URLField(null=True, blank=True)
    headers = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    method = models.CharField(max_length=10, null=True, blank=True)


class ResponseLog(MetaFields):
    status_code = models.IntegerField(null=True, blank=True)
    headers = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)


from django.db import models
from django.forms import ValidationError

from globals import BATCH_CHOICES, CHOICES, CURRENT_BATCH


class CurrentBatchManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(batch=CURRENT_BATCH)


class CurrentBatchMeta(models.Model):
    class Meta:
        abstract = True
        default_manager_name = 'objects'

    objects: models.Manager = CurrentBatchManager()


OCCUPATION_CHOICES = ()


class TimeDateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Subscriber(TimeDateMixin, CurrentBatchMeta):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    occupation = models.CharField(max_length=20)
    batch = models.CharField(
        default=CURRENT_BATCH,
        choices=BATCH_CHOICES, max_length=25)

    class Meta:
        unique_together = ('email', 'phone')

    def __str__(self) -> str:
        return f'{self.name}-{self.email}'


class NewsLetter(TimeDateMixin, CurrentBatchMeta):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    subscriber = models.ManyToManyField(Subscriber)
    batch = models.CharField(
        default=CURRENT_BATCH,
        choices=BATCH_CHOICES, max_length=25)

    class Meta:
        verbose_name_plural = 'Newsletters'


class EmailContent(TimeDateMixin):
    subject = models.CharField(max_length=100)
    body = models.TextField()
    from_email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Email Contents'


class StatusEmail(TimeDateMixin):
    status = models.CharField(
        max_length=40, choices=CHOICES, null=True, blank=True)
    subject = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    mail_from = models.EmailField()
    template = models.FileField(
        upload_to='templates/emails/', null=True, blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Status Emails'

    def __str__(self):
        return f'{self.subject}-{self.status}'

    def clean(self) -> None:
        if self.pk is None:
            if self.active:
                if StatusEmail.objects.filter(status=self.status, active=True).exclude(pk=self.id).exists():
                    raise ValidationError(
                        'There is already an active email with this status')


class StatusEmailFiles(TimeDateMixin):
    status_email = models.ForeignKey(
        StatusEmail, related_name='attachments', on_delete=models.CASCADE)
    file = models.FileField(upload_to='templates/emails/attachments/')

    class Meta:
        verbose_name_plural = 'Status Email Files'


class StatusSMS(TimeDateMixin):
    status = models.CharField(
        max_length=40, choices=CHOICES, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Status SMS'

    def clean(self) -> None:
        if self.pk is None:
            if self.active:
                if StatusSMS.objects.filter(status=self.status, active=True).exists():
                    raise ValidationError(
                        'There is already an active sms with this status')

    def __str__(self):
        return f'{self.body}-{self.status}'

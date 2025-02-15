from email.mime import application

from django.db import models

from application.models import ApplicantExtraInformation, TimeDateMixin
from globals import BATCH_CHOICES

# Create your models here.


class ApplicationNewsSource(TimeDateMixin):
    application_info = models.OneToOneField(
        ApplicantExtraInformation, on_delete=models.CASCADE, related_name='newssource')
    information_source = models.CharField(max_length=100)
    information_source_details = models.CharField(
        max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Application News Sources'


class ApplicantWorkingExperience(TimeDateMixin):
    application_info = models.OneToOneField(
        ApplicantExtraInformation, on_delete=models.CASCADE, related_name='workexperience')
    has_working_experience = models.BooleanField(default=False)
    working_experience_details = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Applicant Working Experiences'

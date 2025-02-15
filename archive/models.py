from django.db import models

from analytics.models import *
from application.models import (ApplicantExtraInformation, Application,
                                ApplicationPayment, ApplicationStatus,
                                ApplicationVerification)
from chat.models import ChatRequest, PhoneRequest, SMSRequest
from globals import CURRENT_BATCH
from newsletter.models import *


class ArchiveContentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(batch=CURRENT_BATCH)


class ArchieveApplicationRelatedObjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(application__batch=CURRENT_BATCH)

    class Meta:
        abstract = True


class ApplicationInfoChildObjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(application_info__application__batch=CURRENT_BATCH)

    class Meta:
        abstract = True


class ArchievedContentMeta(models.Model):
    objects = ArchiveContentManager()

    class Meta:
        abstract = True


class ArchieveApplicationRelatedObjectMeta(
    models.Model
):
    objects = ArchieveApplicationRelatedObjectManager()

    class Meta:
        abstract = True


class ArchieveApplicationInfoRelatedObjectMeta(
    models.Model
):
    objects = ApplicationInfoChildObjectManager()

    class Meta:
        abstract = True


class ArchivedApplication(
    Application
):
    objects = ArchiveContentManager()

    class Meta:
        proxy = True
        verbose_name = 'Archived Application'
        verbose_name_plural = 'Archived Applications'


class ArchivedApplicationStatus(
    ArchieveApplicationRelatedObjectMeta, ApplicationStatus
):

    class Meta:
        proxy = True
        verbose_name = 'Archived Application Status'
        verbose_name_plural = 'Archived Application Statuses'


class ArchivedApplicationVerification(
    ArchieveApplicationRelatedObjectMeta, ApplicationVerification,
):
    class Meta:
        proxy = True
        verbose_name = 'Archived Application Verification'
        verbose_name_plural = 'Archived Application Verifications'


class ArchivedApplicantExtraInformation(
    ArchieveApplicationRelatedObjectMeta,    ApplicantExtraInformation
):

    class Meta:
        proxy = True
        verbose_name = 'Archived Applicant Extra Information'
        verbose_name_plural = 'Archived Applicant Extra Informations'


class ArchivedApplicationPayment(
    ArchieveApplicationRelatedObjectMeta, ApplicationPayment
):
    class Meta:
        proxy = True
        verbose_name = 'Archived Application Payment'
        verbose_name_plural = 'Archived Application Payments'


class ArchivedChatRequest(
    ArchievedContentMeta, ChatRequest
):
    class Meta:
        proxy = True
        verbose_name = 'Archived Chat Request'
        verbose_name_plural = 'Archived Chat Requests'


class ArchivedSMSRequest(
        ArchievedContentMeta, SMSRequest
):
    class Meta:
        proxy = True
        verbose_name = 'Archived SMS Request'
        verbose_name_plural = 'Archived SMS Requests'


class ArchivedPhoneRequest(
        ArchievedContentMeta, PhoneRequest
):
    class Meta:
        proxy = True
        verbose_name = 'Archived Phone Request'
        verbose_name_plural = 'Archived Phone Requests'


class ArchievedNewsLetter(ArchievedContentMeta, NewsLetter):
    class Meta:
        proxy = True
        verbose_name = 'Archived News Letter'
        verbose_name_plural = 'Archived News Letters'


class ArchievedSubscriber(ArchievedContentMeta, Subscriber):
    class Meta:
        proxy = True
        verbose_name = 'Archived Subscriber'
        verbose_name_plural = 'Archived Subscribers'


class ArchivedApplicationNewsSource(ArchieveApplicationInfoRelatedObjectMeta, ApplicationNewsSource):
    class Meta:
        proxy = True
        verbose_name = 'Archived Application News Source'
        verbose_name_plural = 'Archived Application News Sources'


class ArchivedApplicantWorkingExperience(ArchieveApplicationInfoRelatedObjectMeta, ApplicantWorkingExperience):
    class Meta:
        proxy = True
        verbose_name = 'Archived Applicant Working Experience'
        verbose_name_plural = 'Archived Applicant Working Experiences'

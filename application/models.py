import logging
import uuid
from datetime import datetime
from statistics import mode

from django.core.mail import EmailMessage, send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.forms import ValidationError
from django.utils import crypto

from globals import BATCH_CHOICES, CHOICES, CURRENT_BATCH
from newsletter.models import EmailContent, StatusEmail, StatusSMS
from newsletter.views import (
    send_awaiting_payment_email,
    send_status_change_email,
    send_status_change_sms,
    send_submitted_email,
)

VENUE_CHOICES = [("sylhet", "Sylhet"), ("dhaka", "Dhaka"), ("savar", "Savar")]
GENDER_CHOICES = [("male", "Male"), ("female", "Female"), ("other", "Other")]
HSC_GROUP_CHOICES = [("science", "Science"), ("commerce", "Commerce"), ("arts", "Arts")]
STUDY_LEVEL_CHOICES = [("hsc", "HSC"), ("a_level", "A-Level")]
YEAR_CHOICES = [(year, year) for year in range(2010, datetime.now().year + 1)]
QUOTA_CHOICES = [
    ("general", "General"),
    ("tribal", "Tribal"),
    ("armed_forces_officer", "Armed Forces Officer"),
    ("armed_force_personnel", "Armed Forces Personnel"),
    ("freedom_fighter", "Freedom Fighter"),
]


class CurrentBatchManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(batch=CURRENT_BATCH)


class ApplicationRelatedObjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(application__batch=CURRENT_BATCH)


class CurrentBatchMeta(models.Model):
    class Meta:
        abstract = True
        default_manager_name = "objects"

    objects: models.Manager = CurrentBatchManager()


class ApplicationRelatedObjectMeta(models.Model):
    class Meta:
        abstract = True
        default_manager_name = "objects"

    objects: models.Manager = ApplicationRelatedObjectManager()


class TimeDateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class Venue(TimeDateMixin):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)


class Application(TimeDateMixin, CurrentBatchMeta):
    id = models.CharField(max_length=7, primary_key=True)
    name = models.CharField(max_length=255)
    # photo = models.ImageField(upload_to="application/photos/")
    venue = models.CharField(max_length=60)
    phone = models.CharField(max_length=15)
    guardians_phone = models.CharField(max_length=15)
    email = models.EmailField()
    date_of_birth = models.DateField()
    study_level = models.CharField(max_length=20, choices=STUDY_LEVEL_CHOICES)
    hsc_reg_no = models.CharField(max_length=55, blank=True)
    hsc_roll = models.CharField(max_length=20, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    hsc_board = models.CharField(max_length=55, blank=True)
    hsc_group = models.CharField(max_length=10, choices=HSC_GROUP_CHOICES, blank=True)
    institution = models.CharField(max_length=255, blank=True)
    passing_year = models.IntegerField(choices=YEAR_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    # nationality = models.CharField(max_length=55)
    district = models.CharField(max_length=75)
    address = models.TextField()
    quota = models.CharField(max_length=75, default="general")
    information_source = models.CharField(max_length=255, null=True, blank=True)
    programme = models.CharField(
        max_length=255, null=True, blank=True, choices=(("CE", "Civil Engineering - CE"),
    ("CSE", "Computer Science and Engineering - CSE"),
    ("EEE", "Electrical and Electronic Engineering - EEE"),
    ("ME", "Mechanical Engineering - ME"),
    ("IPE", "Industrial and Production Engineering - IPE"),
    ("BBA", "Bachelor of Business Administration - BBA"),
    ("MBA", "Master of Business Administration - MBA"),)
    )
    batch = models.CharField(default="BBA11", choices=BATCH_CHOICES, max_length=25)
    # code = models.CharField(unique=True,max_length=7,editable=False)

    class Meta:
        unique_together = ("phone", "date_of_birth", "batch")

    def save(self, *args, **kwargs):
        # check if creating
        if self._state.adding:
            self.id = crypto.get_random_string(length=7).upper()
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    @classmethod
    def get_venues(cls):
        return (
            (venue, venue)
            for venue in cls.objects.values_list("venue", flat=True).distinct()
        )


class ApplicantExtraInformation(TimeDateMixin, ApplicationRelatedObjectMeta):
    application = models.OneToOneField(
        Application, on_delete=models.CASCADE, related_name="details"
    )
    birth_place = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Birth Place"
    )
    marital_status = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Marital Status"
    )
    permanent_address = models.TextField(
        blank=True, null=True, verbose_name="Permanent Address"
    )
    identification_mark = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Identification Mark"
    )
    blood_group = models.CharField(max_length=5, verbose_name="Blood Group")
    name_father = models.CharField(max_length=255, verbose_name="Name of Father")
    work_place_father = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Work Place of Father"
    )
    designation_father = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Designation of Father"
    )
    national_id_father = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="National ID of Father"
    )
    phone_father = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Phone of Father"
    )
    name_mother = models.CharField(max_length=255, verbose_name="Name of Mother")
    work_place_mother = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Work Place of Mother"
    )
    designation_mother = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Designation of Mother"
    )
    national_id_mother = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="National ID of Mother"
    )
    phone_mother = models.CharField(
        max_length=255, blank=True, verbose_name="Phone of Mother"
    )
    study_level = models.CharField(max_length=20, default="ssc")
    ssc_roll = models.CharField(
        max_length=20, verbose_name="SSC Roll", blank=True, null=True
    )
    ssc_board = models.CharField(
        max_length=55, verbose_name="SSC Board", blank=True, null=True
    )
    gpa = models.DecimalField(
        max_digits=3, decimal_places=2, verbose_name="GPA", blank=True, null=True
    )
    ssc_group = models.CharField(
        max_length=55, verbose_name="SSC Group", blank=True, null=True
    )
    institution = models.CharField(max_length=255, blank=True, null=True)
    photo_personal = models.ImageField(
        upload_to="application/photos/applicants/", verbose_name="Photo of Applicant"
    )
    photo_signature = models.ImageField(
        upload_to="application/photos/signatures/", verbose_name="Photo of Signature"
    )
    passing_year = models.IntegerField(null=True, blank=True)

    admit_card = models.FileField(
        upload_to="application/admit_cards/",
        verbose_name="Admit Card",
        blank=True,
        null=True,
    )
    serial = models.CharField(max_length=20, verbose_name="Roll", blank=True, null=True)

    class Meta:
        verbose_name = "Application Extra Information: Photo Upload Phase"
        verbose_name_plural = "Application Extra Information: Photo Upload Phase"

    def __str__(self):
        return f"{self.application}-info"

    @property
    def roll(self):
        return str(4076 + int(self.id))


class ApplicationPayment(TimeDateMixin, ApplicationRelatedObjectMeta):
    application = models.OneToOneField(
        Application, on_delete=models.CASCADE, related_name="applicationpayment"
    )
    transaction_id = models.CharField(max_length=55, unique=True)
    verified = models.BooleanField(
        blank=True, null=True, verbose_name="Payment Verified"
    )
    mail_sent = models.BooleanField(default=False, editable=False)

    class Meta:
        verbose_name_plural = "Payments"

    # def clean(self) -> None:
    #     if self.application.applicationstatus.status not in ['awaiting_payment','under_review']:
    #         raise ValidationError(
    #             "Application is not in awaiting payment status. Please set application status to 'Awaiting Payment'")


class ApplicationStatus(ApplicationRelatedObjectMeta):
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=100, choices=CHOICES, default="application_submitted"
    )
    message = models.TextField(blank=True)
    mail_sent_awaiting_payment = models.BooleanField(default=False, editable=False)
    mail_sent_payment_completed = models.BooleanField(default=False, editable=False)
    mail_sent_download_admit_card = models.BooleanField(default=False, editable=False)

    class Meta:
        verbose_name_plural = "Application Status"

    # def clean(self) -> None:
    #     if self.status != 'application_submitted':
    #         if self.application.applicationverification.verified is not True:
    #             raise ValidationError(
    #                 "Applicant User must be Verified First. Head over to application verification and verify Application")

    #     if self.status == 'approved':
    #         if self.application.applicationpayment.verified is not True:
    #             raise ValidationError(
    #                 "Payment hasn't been verified. Verify the payment first"
    #             )


class ApplicationStatusChangeLog(models.Model):
    application_status = models.ForeignKey(
        ApplicationStatus,
        on_delete=models.CASCADE,
        related_name="applicationstatuschangelog",
    )
    previous_status = models.CharField(max_length=100, choices=CHOICES)
    new_status = models.CharField(max_length=100, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


class ApplicationVerification(ApplicationRelatedObjectMeta):
    application = models.OneToOneField(
        Application, on_delete=models.CASCADE, related_name="applicationverification"
    )
    verified = models.BooleanField(null=True, blank=True)
    verified_information = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Application Verification"

    def __str__(self):
        return f"{self.application_id}"


class AdmitCardTemplate(TimeDateMixin):
    name = models.CharField(max_length=255)
    template = models.FileField(upload_to="application/admit_card_templates/")
    venue = models.CharField(
        max_length=255,
        # choices=Application.get_venues(),
    )
    is_active = models.BooleanField(default=False)


@receiver(post_save, sender=Application)
def add_status(sender, instance, created, **kwargs):
    if kwargs.get("raw", False):
        return False
    if created:
        application_status = ApplicationStatus.objects.create(application=instance)
        ApplicationVerification.objects.create(application=instance)
        # if instance.gpa >= 3 and \
        #         instance.hsc_roll.isdigit() and len(instance.hsc_roll) == 6 and \
        #         instance.hsc_reg_no.isdigit() and len(instance.hsc_reg_no) == 10:
        #     application_status.status = 'awaiting_payment'
        #     application_status.save()
    return instance


@receiver(post_save, sender=ApplicationStatus)
def send_status_changed_mail(sender, instance, created, **kwargs):
    if kwargs.get("raw", False):
        return False
    ApplicationStatusChangeLog.objects.create(
        application_status=instance,
        previous_status=instance.status,
        new_status=instance.status,
    )
    if instance.status == "awaiting_payment":
        send_status_change_sms(
            applications=[instance.application], status=instance.status, countdown=10
        )
    else:
        send_status_change_sms(
            applications=[instance.application], status=instance.status
        )
    # send_status_change_email(
    #     applications=[instance.application], status=instance.status
    return instance


@receiver(post_save, sender=ApplicationPayment)
def add_details(sender, instance, created, **kwargs):
    if kwargs.get("raw", False):
        return False
    if created:
        application_status = ApplicationStatus.objects.get(
            application=instance.application
        )
        application_status.status = "under_review"
        application_status.save()
        return application_status
    else:
        if instance.verified is True:
            send_status_change_sms(
                applications=[instance.application], status="payment_verified"
            )
        elif instance.verified is False:
            send_status_change_sms(
                applications=[instance.application], status="payment_not_verified"
            )
    return instance


@receiver(post_save, sender=ApplicantExtraInformation)
def status_to_photo_submitted(sender, instance, created, **kwargs):
    if kwargs.get("raw", False):
        return False
    if created:
        application_status = ApplicationStatus.objects.get(
            application=instance.application
        )
        application_status.status = "photo_submitted"
        application_status.save()
    return instance

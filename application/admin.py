
import csv
import io
import os
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.db.models import Count, F, Q
from django.db.models.functions import TruncDate, TruncDay
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.template import Template
from django.template.loader import get_template
from django.urls import path, reverse
from django.utils.html import format_html
from docxtpl import DocxTemplate, InlineImage

from newsletter.models import StatusEmail
from newsletter.views import (send_awaiting_payment_email,
                              send_payment_reminder_sms,
                              send_status_change_email, send_status_change_sms)

from .admit_card import generate_admit_card
from .models import (AdmitCardTemplate, ApplicantExtraInformation, Application,
                     ApplicationPayment, ApplicationStatus,
                     ApplicationStatusChangeLog, ApplicationVerification)

# from xhtml2pdf import pisa


admin.site.site_header = "ApplyKoro.Com Administration Portal"
admin.site.site_title = "Join BAUST Khulna Internal Webpage"
admin.site.index_title = "Welcome to JoinarmyIBA Admin Portal"


@admin.action(description='Mark selected applications as "Payment Completed"', permissions=['change'])
def make_payment_completed(modeladmin, request, queryset):
    for application in queryset:
        ApplicationStatus.objects.filter(
            application=application).update(status='payment_completed')


@admin.action(description='Export Selected as CSV', permissions=['view'])
def export_as_csv(self, request=None, queryset=None, extra_fields=None):
    meta = queryset.model._meta
    field_names = [field.name for field in meta.fields]
    if extra_fields:
        field_names = field_names + extra_fields
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}_{}.csv'.format(
        meta, datetime.now())
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    writer.writerow(field_names)
    objects = queryset.filter(
        **request.GET.dict()
    ).values_list(*field_names)
    for obj in objects:
        writer.writerow(obj)
        # writer.writerow([getattr(obj, field) for field in field_names])
    LogEntry.objects.create(
        user=request.user,
        change_message=f"Exported as CSV: {meta.model_name}",
        action_flag=2,
    )
    return response


class ApplicationPaymentInline(admin.StackedInline):
    model = ApplicationPayment


class ApplicantExtraInformationInline(admin.StackedInline):
    model = ApplicantExtraInformation
    extra = 0


class ApplicationStatusInline(admin.StackedInline):

    model = ApplicationStatus


class ApplicationVerificationInline(admin.StackedInline):
    model = ApplicationVerification


class ApplicationAdmin(admin.ModelAdmin):
    change_list_template = "application/admin/application_changelist.html"
    inlines = [ApplicantExtraInformationInline,
               ApplicationStatusInline,
               ApplicationPaymentInline,
               ApplicationVerificationInline]
    readonly_fields = ['id', 'user_photo',
                       'user_signature', ]
    list_filter = ('batch', 'passing_year', 'created_at', 'applicationstatus__status',
                   'applicationpayment__verified',
                   'applicationverification__verified',
                   'gender', 'venue',  'district',
                   'information_source', 'institution',
                   )
    list_display = ('id', 'user_verified', 'payment_verified', 'photo_uploaded', 'name', 'email', 'gender',
                    'phone',
                    'status', 'created_at', 'information_source')
    ordering = ('created_at',)

    search_fields = ['id', 'name', 'phone', 'email']
    fieldsets = (
        ("Application Details",
         {'fields': ('id', 'venue', 'quota', 'programme', 'information_source')}),
        ("Personal Information", {
            'fields': ('user_photo', 'user_signature', 'name',  'phone', 'guardians_phone', 'email', 'date_of_birth', 'gender', 'address', 'district')
        }),
        ('Educational Information', {

            'fields': ('study_level', 'gpa', 'institution', 'passing_year'),
        }),

        ('HSC', {
            # 'classes': ('collapse',),
            'fields': ('hsc_roll', 'hsc_reg_no', 'hsc_group', 'hsc_board'),
        }),)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('approve/', self.primary_select),
            path('approve-payments/', self.approve_verified_payments),
            path('download-all-csv/', self.download_all_csv),

        ]
        return custom_urls+urls

    def download_all_csv(self, request):
        return export_as_csv(self, request,
                             queryset=Application.objects.all()
                             )

    def primary_select(self, request):
        """initial approval of application so that user make payment
        """
        application_statuses = ApplicationStatus.objects.filter(application__gpa__gte=3.5,
                                                                # application__applicationverification__verified=True,
                                                                # application__created_at__lte=datetime.now()-timedelta(hours=8),
                                                                status='application_submitted'
                                                                )
        application_emails = []
        for application_status in application_statuses:
            application_status.status = 'awaiting_payment'
            application_status.mail_sent_awaiting_payment = True
            application_status.save()
            # application_emails.append(application_status.application)
        # send_status_change_email(
        #     applications=application_emails, status='awaiting_payment')
        # send_awaiting_payment_email(application_emails)
        self.message_user(
            request, 'Primary Approved all applications with GPA over 3.5 and sent confirmation emails')
        return HttpResponseRedirect("../")

    def approve_verified_payments(self, request):
        application_payments = ApplicationPayment.objects.filter(
            verified=True, mail_sent=False)
        application_statuses = ApplicationStatus.objects.filter(application__in=application_payments.values(
            'application'), status='under_review')

        for application_status in application_statuses:
            application_status.status = 'payment_completed'
            application_status.mail_sent_payment_completed = True
            application_status.save()

        application_payments.update(mail_sent=True)
        self.message_user(
            request, 'Approved application with verified payments')
        return HttpResponseRedirect("../")

    def user_photo(self, obj):
        return format_html(
            '<img   loading="lazy" src="{}" width="100" height="100" />',
            obj.details.photo_personal.url
        )

    def user_signature(self, obj):
        return format_html(
            '<img  loading="lazy" src="{}" width="100" height="30" />',
            obj.details.photo_signature.url
        )

    def status(self, obj):
        return obj.applicationstatus.get_status_display()

    def user_verified(self, obj):
        return obj.applicationverification.verified

    def payment_verified(self, obj):
        return obj.applicationpayment.verified

    @admin.display(description="Photo Uploaded")
    def photo_uploaded(self, obj):
        return True if obj.details else False

    photo_uploaded.boolean = True
    user_verified.boolean = True
    payment_verified.boolean = True
    # def changelist_view(self, request, extra_context=None):
    #     response = super().changelist_view(request, extra_context=extra_context)
    #     per_day_count= list(response.context_data["cl"].queryset.annotate(date=TruncDate('created_at')).values('date').annotate(count=Count('id')).order_by('-date'))
    #     extra_context={'per_day_count' : per_day_count}
    #     response.context_data.update(extra_context)
    #     return response


class ApplicationStatusAdmin(admin.ModelAdmin):
    model = ApplicationStatus
    list_display = ('application_id', 'status',
                    'mail_sent_awaiting_payment', 'mail_sent_payment_completed',)
    # actions = [export_as_csv]
    search_fields = ['application__id']
    list_filter = ('application__batch', 'status',)
    readonly_fields = ['mail_sent_awaiting_payment',
                       'mail_sent_payment_completed', ]


class ApplicationPaymentAdmin(admin.ModelAdmin):
    change_list_template = "application/admin/payment_changelist.html"
    list_filter = (
        'application__batch', 'created_at', 'application__applicationstatus__status', 'verified', )
    ordering = ('created_at',)
    search_fields = ['transaction_id', 'application__id']
    model = ApplicationPayment
    readonly_fields = ['mail_sent']
    list_display = ('application_id', 'transaction_id', 'verified', 'applicant_name',
                    'applicant_phone', 'applicant_email',
                    'status')
    # actions = [export_as_csv]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('approve-payments/', self.approve_verified_payments),
            path('download-all-csv/', self.download_all_csv),
            path('send-payment-reminder/', self.send_payment_reminder),
            path('send-payment-reminder/guardian/',
                 self.send_payment_reminder, kwargs={'to_guardian': True}),
        ]
        return custom_urls+urls

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        ordered_by_verified = ApplicationPayment.objects.order_by('verified')
        extra_context['order_by_verified'] = ordered_by_verified

        return super().changelist_view(request, extra_context)

    def status(self, obj):
        return obj.application.applicationstatus.get_status_display()

    def applicant_name(self, obj):
        return obj.application.name

    def applicant_phone(self, obj):
        return obj.application.phone

    def applicant_email(self, obj):
        return obj.application.email

    def download_all_csv(self, request):
        return export_as_csv(self,
                             request,
                             extra_fields=['application__name',
                                           'application__phone',
                                           'application__guardians_phone',
                                           'application__email',
                                           'application__address'],
                             queryset=ApplicationPayment.objects.all())

    def approve_verified_payments(self, request):
        application_payments = ApplicationPayment.objects.filter(
            verified=True, mail_sent=False)
        application_statuses = ApplicationStatus.objects.filter(application__in=application_payments.values(
            'application'), status='under_review')

        for application_status in application_statuses:
            application_status.status = 'payment_completed'
            application_status.mail_sent_payment_completed = True
            application_status.save()

        application_payments.update(mail_sent=True)
        self.message_user(
            request, 'Marked application with verified payments as Payment Completed')
        return HttpResponseRedirect("../")

    def send_payment_reminder(self, request, *args, **kwargs):
        """send sms to users who have not paid, but have not received a reminder yet.
        for Status: "awaiting_payment"

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        application_statuses = ApplicationStatus.objects.filter(
            status__in=['awaiting_payment', 'payment_not_received']).values_list(
            'application', flat=True)
        applications = Application.objects.filter(id__in=application_statuses)
        chunks = [applications[i:i+50]
                  for i in range(0, len(applications), 50)]
        for chunk in chunks:
            send_payment_reminder_sms(
                applications=chunk, status='awaiting_payment_reminder', to_guardian=kwargs.get('to_guardian'))
        send_status_change_email(
            applications=applications, status='awaiting_payment_reminder')

        self.message_user(
            request, f'Notified users or guardians who have not paid.')
        return HttpResponseRedirect("../../")


class ApplicationVerificationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Application Info', {
            'fields': ('application', 'study_level', 'name', 'hsc_roll',
                       'hsc_reg_no', 'hsc_board', 'passing_year', 'date_of_birth')
        }),
        ('Verification Info', {
            'fields': ('verified', 'verified_information')
        }),

    )
    ordering = ('application__created_at',)
    readonly_fields = ('application', 'study_level', 'name', 'hsc_roll',
                       'hsc_reg_no', 'hsc_board', 'passing_year', 'date_of_birth')
    list_display = ('application_id', 'verified', 'name', 'date_of_birth',
                    'hsc_roll', 'hsc_reg_no', 'hsc_board', 'passing_year', 'study_level'
                    )
    list_filter = ('application__batch', 'verified', 'application__study_level',
                   )

    def study_level(self, obj):
        return obj.application.study_level

    def hsc_roll(self, obj):
        return obj.application.hsc_roll

    def hsc_reg_no(self, obj):
        return obj.application.hsc_reg_no

    def date_of_birth(self, obj):
        return obj.application.date_of_birth

    def passing_year(self, obj):
        return obj.application.passing_year

    def hsc_board(self, obj):
        return obj.application.hsc_board

    def name(self, obj):
        return obj.application.name


class LogEntriesAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
    list_display = ('id', 'user', 'content_type',
                    'change_message', 'action_time',)


class ApplicantExtraInformationAdmin(admin.ModelAdmin):
    change_list_template = 'application/admin/applicant_extra_information_changelist.html'
    search_fields = ['application__id', 'application__name', 'serial']
    list_display = ('application_id', 'applicant_name', 'personal_photo', 'signature_photo', 'applicant_phone', 'applicant_email', 'serial', 'admit_uploaded',
                    'has_working_experience', 'news_source', 'created_at',
                    'download_report'
                    )
    readonly_fields = ['personal_photo', 'signature_photo', ]
    list_filter = ('application__batch', 'blood_group',
                   'application__gender', 'application__venue', 'institution')

    @admin.display(description='Admit Uploaded')
    def admit_uploaded(self, obj):
        return obj.admit_card != ''

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('download-all-csv/', self.download_all_csv),
            path('download-dhaka-csv/', self.download_dhaka_csv),
            path('download-file/<application_id>', self.download_file,
                 name='application_applicantextrainformationAdmin_download-file'),
            path('remind-download-admit/', self.remind_download_admit),
            path('remind-upload-photo/', self.remind_upload_photo),
            path('send-venue-location-sylhet/',
                 self.send_venue_location_sylhet),
            path('send-venue-location-dhaka/', self.send_venue_location_dhaka),
            path('send-dummy-venue-location/',
                 self.send_dummy_venue_location_for_awaiting_payment),
        ]
        return custom_urls+urls

    def download_dhaka_csv(self, request):
        meta = Application._meta
        field_names = [f'application__{field.name}' for field in meta.fields]
        return export_as_csv(self=self, request=request, queryset=ApplicantExtraInformation.objects.filter(application__venue='Dhaka'),
                             extra_fields=field_names)

    def remind_download_admit(self, request):
        application_statuses = ApplicationStatus.objects.filter(
            status='photo_submitted').values_list(
            'application', flat=True)
        applications = Application.objects.filter(id__in=application_statuses)
        send_status_change_sms(
            applications=applications, status='download_admit')
        self.message_user(request, 'Reminded users to download admit card')
        return HttpResponseRedirect("../")

    def remind_upload_photo(self, request):
        application_statuses = ApplicationStatus.objects.filter(
            status='payment_completed').values_list(
            'application', flat=True)
        applications = Application.objects.filter(id__in=application_statuses)
        send_status_change_sms(
            applications=applications, status='remind_upload_photo')
        self.message_user(request, 'Reminded users to upload photo')
        return HttpResponseRedirect("../")

    def send_venue_location_sylhet(self, request):
        applications = Application.objects.filter((Q(applicationstatus__status='payment_completed') | Q(applicationstatus__status='photo_submitted'))
                                                  & Q(venue='Sylhet'))
        send_status_change_sms(
            applications=applications, status='notify_venue_as_sylhet')
        self.message_user(request, 'Notified')
        return HttpResponseRedirect("../")

    def send_venue_location_dhaka(self, request):
        applications = Application.objects.filter((Q(applicationstatus__status='payment_completed') | Q(applicationstatus__status='photo_submitted'))
                                                  & Q(venue='Dhaka'))
        send_status_change_sms(
            applications=applications, status='notify_venue_as_dhaka')
        self.message_user(request, 'Notified')
        return HttpResponseRedirect("../")

    def send_dummy_venue_location_for_awaiting_payment(self, request):
        applications = Application.objects.filter(Q(applicationstatus__status='awaiting_payment')
                                                  & Q(venue__icontains='Mirpur'))
        send_status_change_sms(
            applications=applications, status='notify_dummy_venue_location')
        self.message_user(request, 'Notified')
        return HttpResponseRedirect("../")

    def download_file(self, request, application_id):
        application = Application.objects.filter(
            id=application_id, applicationstatus__status='photo_submitted').first()
        if application:
            admit_card_file = generate_admit_card(application)
            return FileResponse(open(admit_card_file, 'rb'), as_attachment=True, filename='admit_card.pdf')

    def download_all_csv(self, request):
        meta = Application._meta
        field_names = [f'application__{field.name}' for field in meta.fields]
        return export_as_csv(self=self, request=request, queryset=ApplicantExtraInformation.objects.all(),
                             extra_fields=field_names)

    @admin.display(description='Download Application')
    def download_report(self, obj):
        return format_html(
            '<a href="{}">Download file</a>',
            reverse('admin:application_applicantextrainformationAdmin_download-file',
                    args=[obj.application.id])
        )

    @admin.display(description='Applicants Photo')
    def personal_photo(self, obj):
        return format_html(
            '<img loading="lazy" src="{}" width="100" height="100" />',
            obj.photo_personal.url
        )

    @admin.display(description='Applicants Signature')
    def signature_photo(self, obj):
        return format_html(
            '<img loading="lazy" src="{}" width="100" height="20" />',
            obj.photo_signature.url
        )

    @admin.display(description='Name')
    def applicant_name(self, obj):
        return obj.application.name

    @admin.display(description='Phone')
    def applicant_phone(self, obj):
        return obj.application.phone

    @admin.display(description='Email')
    def applicant_email(self, obj):
        return obj.application.email

    @admin.display(description='Has Working Experience')
    def has_working_experience(self, obj):
        return obj.workexperience.has_working_experience

    @admin.display(description='Source')
    def news_source(self, obj):
        return obj.newssource.information_source
    has_working_experience.boolean = True
    admit_uploaded.boolean = True


admin.site.register(ApplicantExtraInformation,
                    ApplicantExtraInformationAdmin)
admin.site.register(LogEntry, LogEntriesAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(ApplicationPayment, ApplicationPaymentAdmin)
admin.site.register(ApplicationStatus, ApplicationStatusAdmin)
admin.site.register(ApplicationVerification, ApplicationVerificationAdmin)
admin.site.register(ApplicationStatusChangeLog)
admin.site.register(AdmitCardTemplate)

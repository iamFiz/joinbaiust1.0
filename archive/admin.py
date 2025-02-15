from django.contrib import admin

from analytics.admin import *
from application.admin import *
from chat.admin import *
from newsletter.admin import *

from .models import *

# Register your models here.
admin.site.register(ArchivedApplication, ApplicationAdmin)

admin.site.register(ArchivedApplicationStatus, ApplicationStatusAdmin)

admin.site.register(ArchivedApplicationVerification,
                    ApplicationVerificationAdmin)

admin.site.register(ArchivedApplicantExtraInformation,
                    ApplicantExtraInformationAdmin)

admin.site.register(ArchivedApplicationPayment,
                    ApplicationPaymentAdmin)

admin.site.register(ArchivedChatRequest, ChatRequestAdmin)
admin.site.register(ArchivedSMSRequest, SMSRequestAdmin)
admin.site.register(ArchivedPhoneRequest, PhoneRequestAdmin)
admin.site.register(ArchievedNewsLetter, NewsLetterAdmin)
admin.site.register(ArchievedSubscriber, SubscriberAdmin)

admin.site.register(
    ArchivedApplicantWorkingExperience, ApplicationWorkingExperienceAdmin)
admin.site.register(
    ArchivedApplicationNewsSource,
    ApplicationNewsSourceAdmin
)

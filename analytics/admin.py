from django.contrib import admin

# Register your models here.
from .models import ApplicantWorkingExperience, ApplicationNewsSource


class ApplicationWorkingExperienceAdmin(admin.ModelAdmin):
    list_display = ('get_application_id', 'has_working_experience',
                    )
    search_fields = ('application_info__application__id',)
    list_filter = ('application_info__application__batch',
                   'has_working_experience',)

    @admin.display(description='Application ID')
    def get_application_id(self, obj):
        return obj.application_info.application.id


class ApplicationNewsSourceAdmin(admin.ModelAdmin):

    change_list_template = 'analytics/admin/newssource_changelist.html'
    search_fields = ('application_info__application__id',)
    list_display = ('get_application_id', 'information_source',
                    )
    list_filter = ('application_info__application__batch',
                   'information_source',)
    search_fields = ('application_info__application__id',
                     )
    ordering = ('information_source',)

    @admin.display(description='Application ID')
    def get_application_id(self, obj):
        return obj.application_info.application.id


admin.site.register(ApplicantWorkingExperience,
                    ApplicationWorkingExperienceAdmin)
admin.site.register(ApplicationNewsSource, ApplicationNewsSourceAdmin)

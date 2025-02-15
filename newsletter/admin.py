from django.contrib import admin

from newsletter.models import (EmailContent, NewsLetter, StatusEmail,
                               StatusEmailFiles, StatusSMS, Subscriber)


class StatusEmailFilesInline(admin.TabularInline):
    model = StatusEmailFiles
    extra = 0


class StatusEmailAdmin(admin.ModelAdmin):
    inlines = [StatusEmailFilesInline]
    list_display = ['status', 'body']


class StatusSMSAdmin(admin.ModelAdmin):
    list_display = ['status', 'body']


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'occupation']
    list_filter = ['batch']


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'date']
    list_filter = ['batch']


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(NewsLetter, NewsLetterAdmin)
admin.site.register(StatusEmail, StatusEmailAdmin)
admin.site.register(StatusEmailFiles)
admin.site.register(StatusSMS, StatusSMSAdmin)
# admin.site.register(EmailContent)

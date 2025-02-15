from django.contrib import admin

from chat.models import ChatRequest, PhoneRequest, SMSRequest


class ChatRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'name', 'phone',
                    'email', 'application_id',  'message', 'problem_type', 'created_at')
    list_filter = ('batch', 'status', 'response_via', 'problem_type')
    search_fields = ('name', 'phone', 'email',
                     'message__icontains', 'application_id__icontains')


class SMSRequestAdmin(admin.ModelAdmin):
    list_display = ('assigned_to', 'responded', 'phone', 'application_id', 'problem', 'problem_type',
                    'created_at')
    list_filter = ('responded',  'batch', 'response_via',
                   'assigned_to', 'problem_type')
    search_fields = ('phone', 'problem__icontains',
                     'application_id__icontains')


class PhoneRequestAdmin(admin.ModelAdmin):
    list_display = ('assigned_to', 'responded', 'phone','application_id', 'problem', 'problem_type',
                    'created_at')
    list_filter = ('responded',  'batch', 'response_via',
                   'assigned_to', 'problem_type')
    search_fields = ('phone', 'problem__icontains',
                     'application_id__icontains')


admin.site.register(ChatRequest, ChatRequestAdmin)
admin.site.register(SMSRequest, SMSRequestAdmin)
admin.site.register(PhoneRequest, PhoneRequestAdmin)

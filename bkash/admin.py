from django.contrib import admin

from .models import PaymentReference, RequestLog, ResponseLog


@admin.register(PaymentReference)
class PaymentReferenceAdmin(admin.ModelAdmin):
    list_display = ['payer_reference', 'merchant_invoice_number', 'status']
    list_filter = ['status']
    search_fields = ['payer_reference', 'merchant_invoice_number']
    readonly_fields = ['payer_reference',
                       'merchant_invoice_number', 'status', 'payment_id']
    fieldsets = (
        (None, {
            'fields': ('payer_reference', 'merchant_invoice_number', 'status', 'payment_id')
        }),
    )

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

from django.contrib import admin
from .models import Business


class BusinessAdminVeiw(admin.ModelAdmin):
    list_filter = ('business_name','owner__first_name')
    list_display = ('business_name', 'uuid',)
    readonly_fields = ('uuid','payment_account_number')

    
    fieldsets = (
        (None, {'fields': ('owner','uuid', 'payment_account_number',
        'property_description')}),
                )

    search_fields = ('business_name','owner__first_name')
    filter_horizontal = ()        
admin.site.register(Business,BusinessAdminVeiw)

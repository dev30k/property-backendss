from django.contrib import admin
from .models import *



class ResidentailPropertyInline(admin.TabularInline):
    model = ResidentailProperty

class CommercialPropertyInline(admin.TabularInline):
    model = CommercialProperty


class PropertyAdminVeiw(admin.ModelAdmin):
    list_filter = ('property_name','landlord__first_name')
    list_display = ('property_name','landlord','address','county',)


    

    search_fields = ('property_name','landlord',)
    filter_horizontal = ()    
    inlines = [
        ResidentailPropertyInline,
        CommercialPropertyInline
    ]

admin.site.register(Property,PropertyAdminVeiw)



from django.contrib.auth.models import Group
from django import forms
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from apps.users.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin
from apps.users.models import MyUser



# Register your models here.
class MyUserAdminView(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_filter = ('nat_id','email')
    list_display = ('first_name', 'last_name', 'nat_id',
            'email', 'phone_number',)

    
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'nat_id',
            'email', 'phone_number','password')}),
                ('Group Permissions', {
            'fields': ('groups', 'user_permissions', )
        }),)
    add_fieldsets = (
        (None, {'fields': ('first_name','last_name','nat_id','email','password1', 'password2')}),
    )


    search_fields = ('nat_id',)
    ordering = ('email',)
    filter_horizontal = ()        

admin.site.unregister(Group)
admin.site.register(MyUser, MyUserAdminView)
from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(CartList)

from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from forms import RegisterForm, UserChangeForm

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = RegisterForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['userName', 'name', 'callNumber', 'address', "is_active", "is_seller", "is_admin"]
    list_filter = ["is_seller", "is_admin"]
    fieldsets = [
        (None, {"fields": ['userName', 'name', "password"]}),
        ("Personal info", {"fields": ['callNumber', 'address']}),
        ("Permissions", {"fields": ["is_active", "is_seller", "is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ['userName', 'name', 'callNumber', 'address', "password1", "password2"],
            },
        ),
    ]
    search_fields = ['userName']
    ordering = ['userName']
    filter_horizontal = []




# Now register the new UserAdmin...
admin.site.register(myUser, UserAdmin)

admin.site.unregister(Group)
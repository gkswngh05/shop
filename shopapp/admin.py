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
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = myUser
        fields = ['userName', 'name', 'callNumber', 'address']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = myUser
        fields = ['userName', 'name', 'callNumber', 'address', "is_active", "is_seller", "is_admin"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

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
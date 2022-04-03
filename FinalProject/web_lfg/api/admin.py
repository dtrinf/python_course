from django.contrib import admin
# User lib
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'twitter_user']
    # Required to add the fields to the admin page
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'twitter_user', 'password1', 'password2')}
        ),
    )


# Custom user and form registration
admin.site.register(CustomUser, CustomUserAdmin)


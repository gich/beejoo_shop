from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from sb_auth.models import CustomUser
# Register your models here.

class CustomAdminModel(UserAdmin):
    list_display = (
        'username',
        'first_name',
        'note'
    )

admin.site.register(CustomUser, CustomAdminModel)
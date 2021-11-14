from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ITIUser
from .froms import UserAdminForm


class CustomUserAdmin(UserAdmin):
    form = UserAdminForm
    list_display = (
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "email",
        "mobile_number",
    )
    fieldsets = (
        (
            None,
            {
                "fields": ("username", "password"),
            },
        ),
        (
            "Personal info",
            {
                "fields": ("first_name", "last_name", "email", "mobile_number"),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "Important dates",
            {
                "fields": ("last_login", "date_joined"),
            },
        ),
    )


admin.site.register(ITIUser, CustomUserAdmin)

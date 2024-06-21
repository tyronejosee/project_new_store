"""Admin for Users App."""

from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Admin for CustomUser model."""

    search_fields = ("username", "email")
    list_display = (
        "username",
        "email",
        "date_joined",
        "is_active",
    )
    list_per_page = 25
    readonly_fields = ("pk", "date_joined", "last_login", "password")
    ordering = ("pk",)

"""Admin for Users App."""

from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Admin config for the CustomUser model."""
    list_display = ('username', 'email', 'date_joined', 'is_active',)
    ordering = ('username',)

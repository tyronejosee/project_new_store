"""Admin for Home App."""

from django.contrib import admin
from home.models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Admin configuration for the Page model."""
    list_display = ('title', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('title',)

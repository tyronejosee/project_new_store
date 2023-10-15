"""Admin for Home App."""

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from home.models import Page


class PageResource(resources.ModelResource):
    """Class for importing and exporting data for the Page model."""
    class Meta:
        model = Page


@admin.register(Page)
class PageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin configuration for the Page model."""
    list_display = ('key', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('key',)
    resource_class = PageResource

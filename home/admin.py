"""Admin for Home App."""

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from home.models import Company, Page


class CompanyResource(resources.ModelResource):
    """Class for importing and exporting data."""
    class Meta:
        """Meta definition for CompanyResource"""
        model = Company


class PageResource(resources.ModelResource):
    """Class for importing and exporting data."""
    class Meta:
        """Meta definition for PageResource"""
        model = Page


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Admin config for the Company model."""
    list_display = ("name",)
    readonly_fields = ("pk",)
    resource_class = CompanyResource


@admin.register(Page)
class PageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin config for the Page model."""
    search_fields = ("key",)
    list_display = ("key", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 25
    readonly_fields = ("pk",)
    ordering = ("pk",)
    resource_class = PageResource

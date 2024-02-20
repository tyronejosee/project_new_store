"""Admin for Home App."""

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from home.models import Company, Page


class CompanyResource(resources.ModelResource):
    """Class for importing and exporting data for the Company model."""
    class Meta:
        """Meta definition for CompanyResource"""
        model = Company


class PageResource(resources.ModelResource):
    """Class for importing and exporting data for the Page model."""
    class Meta:
        """Meta definition for PageResource"""
        model = Page


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Admin config for the Company model."""
    list_display = ("name",)
    resource_class = CompanyResource


@admin.register(Page)
class PageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin config for the Page model."""
    list_display = ("key", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("key",)
    resource_class = PageResource

    def save_model(self, request, obj, form, change):
        # Remove the image when clearing the path on the page
        if change and "image" in form.changed_data:
            old_page = Page.objects.get(pk=obj.pk)
            old_page.image.delete(save=False)
        super().save_model(request, obj, form, change)

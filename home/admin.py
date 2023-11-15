"""Admin for Home App."""

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from home.models import Company, Page


class PageResource(resources.ModelResource):
    """Class for importing and exporting data for the Page model."""
    class Meta:
        model = Page


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Admin configuration for the Company model."""


@admin.register(Page)
class PageAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin configuration for the Page model."""
    list_display = ('key', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('key',)
    resource_class = PageResource

    def save_model(self, request, obj, form, change):
        "Override the save_model method to remove the image when clearing the path in the page."
        if change and 'image' in form.changed_data:
            old_product = Page.objects.get(pk=obj.pk)
            old_product.image.delete(save=False)
        super().save_model(request, obj, form, change)

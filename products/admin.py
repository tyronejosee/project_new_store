"""Admin for Products App."""

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from products.models import Product, Deal, Category, Brand
from utils.actions import ActionsMixin


class CategoryResource(resources.ModelResource):
    """Class for importing and exporting data for the Category model."""

    class Meta:
        model = Category


class BrandResource(resources.ModelResource):
    """Class for importing and exporting data for the Brand model."""

    class Meta:
        model = Brand


class ProductResource(resources.ModelResource):
    """Class for importing and exporting data for the Product model."""

    class Meta:
        model = Product


class DealResource(resources.ModelResource):
    """Class for importing and exporting data for the Deal model."""

    class Meta:
        model = Deal


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, ActionsMixin):
    """Admin config for the Category model."""

    search_fields = ("title",)
    list_display = (
        "title",
        "show_hide",
    )
    list_filter = ("show_hide",)
    list_per_page = 25
    readonly_fields = ("pk", "slug")
    ordering = ("pk",)
    resource_class = CategoryResource


@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin, ActionsMixin):
    """Admin config for the Brand model."""

    search_fields = ("name",)
    list_display = ("name",)
    list_filter = ("show_hide",)
    list_per_page = 25
    readonly_fields = ("pk", "slug")
    ordering = ("pk",)
    resource_class = BrandResource


@admin.register(Deal)
class DealAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin config for the Deal model."""

    search_fields = ("name", "description")
    list_display = ("name", "discount", "start_date", "end_date", "status")
    list_filter = ("status",)
    list_per_page = 25
    readonly_fields = ("pk", "slug")
    ordering = ("pk",)
    resource_class = DealResource


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, ActionsMixin):
    """Admin config for the Product model."""

    search_fields = ("title",)
    list_display = ("title", "normal_price", "brand", "updated_at")
    list_filter = ("show_hide",)
    list_per_page = 25
    readonly_fields = ("pk", "slug", "created_at", "updated_at", "sale_price")
    ordering = ("pk",)
    resource_class = ProductResource

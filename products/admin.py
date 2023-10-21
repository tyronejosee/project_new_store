"""Admin for Products App."""

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from products.models import Product, Deal, Category, Brand, ProductDeal


# Import-Export Class

class CategoryResource(resources.ModelResource):
    """Class for importing and exporting data for the Category model."""
    class Meta:
        model = Category


class BrandResource(resources.ModelResource):
    """Class for importing and exporting data for the Brand model."""
    class Meta:
        model = Brand


class DealResource(resources.ModelResource):
    """Class for importing and exporting data for the Deal model."""
    class Meta:
        model = Deal


class ProductResource(resources.ModelResource):
    """Class for importing and exporting data for the Product model."""
    class Meta:
        model = Product


class ProductDealResource(resources.ModelResource):
    """Class for importing and exporting data for the ProductDeal model."""
    class Meta:
        model = ProductDeal


# Models Class

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin config for the Category model."""
    list_display = ('title', 'section', 'show_hide',)
    ordering = ('section', 'title',)
    resource_class = CategoryResource


@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin config for the Brand model."""
    list_display = ('name', 'show_hide',)
    ordering = ('name',)
    resource_class = BrandResource


@admin.register(Deal)
class DealAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin config for the Deal model."""
    list_display = ('name', 'discount', 'start_date', 'end_date')
    ordering = ('-start_date',)
    resource_class = DealResource


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin config for the Product model."""
    list_display = ('title', 'normal_price', 'category',
                    'brand', 'stock', 'featured', 'show_hide')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    resource_class = ProductResource

    class Media:
        """Additional configuration for CKEditor."""
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }


@admin.register(ProductDeal)
class ProductDealAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin config for the ProductDeal model."""
    list_display = ('product', 'deal')
    ordering = ('-product',)
    resource_class = ProductDealResource

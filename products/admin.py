"""Admin for Products App."""

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from products.models import Product, Deal, Category, Brand


# Import-Export Class

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


# Models Class

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin config for the Category model."""
    list_display = ('title', 'slug', 'show_hide',)
    ordering = ('pk',)
    resource_class = CategoryResource


@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin config for the Brand model."""
    list_display = ('name', 'slug', 'show_hide',)
    ordering = ('pk',)
    resource_class = BrandResource


@admin.register(Deal)
class DealAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin config for the Deal model."""
    list_display = ('name', 'slug', 'image', 'discount', 'start_date', 'end_date')
    ordering = ('pk',)
    resource_class = DealResource

    def save_model(self, request, obj, form, change):
        # Remove the image when clearing the path in the deal
        if change and 'image' in form.changed_data:
            old_deal = Deal.objects.get(pk=obj.pk)
            old_deal.image.delete(save=False)
        super().save_model(request, obj, form, change)


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin config for the Product model."""
    list_display = ('title', 'updated_at', 'slug', 'normal_price',
                    'brand', 'stock', 'show_hide')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title',)
    ordering = ('updated_at', 'pk',)
    resource_class = ProductResource

    class Media:
        """Additional config for CKEditor."""
        css = {
            'all': ('css/ckeditor.css',)
        }

    def save_model(self, request, obj, form, change):
        # Remove the image when clearing the path in the prod.
        if change and 'image' in form.changed_data:
            old_product = Product.objects.get(pk=obj.pk)
            old_product.image.delete(save=False)
        super().save_model(request, obj, form, change)

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
    list_display = ('title', 'show_hide',)
    ordering = ('title',)
    resource_class = CategoryResource


@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin config for the Brand model."""
    list_display = ('name', 'show_hide',)
    ordering = ('name',)
    resource_class = BrandResource


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

    def save_model(self, request, obj, form, change):
        "Override the save_model method to remove the image when clearing the path in the prod."
        if change and 'image' in form.changed_data:
            old_product = Product.objects.get(pk=obj.pk)
            old_product.image.delete(save=False)
        super().save_model(request, obj, form, change)


@admin.register(Deal)
class DealAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """Admin config for the Deal model."""
    list_display = ('name', 'discount', 'start_date', 'end_date')
    ordering = ('-start_date',)
    resource_class = DealResource

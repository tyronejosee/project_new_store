"""Admin for Products App."""
from django.contrib import admin

from products.models import Product, Category, Brand


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for the Category model."""
    list_display = ('title', 'section', 'show_hide',)
    ordering = ('section', 'title',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Admin configuration for the Brand model."""
    list_display = ('name', 'show_hide',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin configuration for the Product model."""
    list_display = ('title', 'normal_price', 'category', 'brand', 'stock', 'featured', 'show_hide')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    class Media:
        """Extra: CKEditor CSS."""
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

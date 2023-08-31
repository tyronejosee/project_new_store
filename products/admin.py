"""Admin Configuration for Store Models."""
from django.contrib import admin
from products.models import Product, Category, Brand


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for the Category model."""
    list_display = ('title', 'show_hide',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('title',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Admin configuration for the Brand model."""
    list_display = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin configuration for the Product model."""
    list_display = ('title', 'category', 'normal_price', 'stock', 'featured', 'show_hide')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('title',)
    list_filter = ('category__title',)
    search_fields = ('title', 'category__title') # debo extender este campo

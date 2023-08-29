"""Admin Configuration for Store Models."""

from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin configuration for the Product model."""
    list_display = ('title', 'category', 'price')
    ordering = ('title',)
    list_filter = ('category',)
    search_fields = ('title', 'category__title')

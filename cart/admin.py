"""Admin for Cart App."""

from django.contrib import admin
from cart.models import Cart, Wishlist, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """Admin config for the Cart model."""
    search_fields = ("user",)
    list_per_page = 25
    readonly_fields = ("pk",)
    ordering = ("pk",)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """Admin config for the CartItem model."""
    search_fields = ("cart",)
    list_per_page = 25
    readonly_fields = ("cart", "product", "quantity")
    ordering = ("pk",)


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """Admin config for the Wishlist model."""
    search_fields = ("user",)
    list_per_page = 25
    readonly_fields = ("pk",)
    ordering = ("pk",)

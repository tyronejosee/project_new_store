"""Admin for Cart App."""

from django.contrib import admin
from cart.models import Cart, Wishlist, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """Admin config for the Cart model."""
    ordering = ('-user',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """Admin config for the CartItem model."""


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """Admin config for the Wishlist model."""
    ordering = ('-user',)

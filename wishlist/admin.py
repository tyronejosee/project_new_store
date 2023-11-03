"""Admin for Wishlist App."""

from django.contrib import admin
from wishlist.models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """Admin config for the Wishlist model."""
    ordering = ('-user',)
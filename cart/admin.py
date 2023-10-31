"""Admin for Products App."""

from django.contrib import admin
from cart.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """Admin config for the Cart model."""
    ordering = ('-user',)

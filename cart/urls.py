"""URLs for Cart App."""

from django.urls import path
from cart.views import store, add_product, remove_product, subtract_product, clear_cart

urlpatterns = [
    path('', store, name="store"),
    path('add/<int:product_id>/', add_product, name="Add"),
    path('remove/<int:product_id>/', remove_product, name="Del"),
    path('subtract/<int:product_id>/', subtract_product, name="Sub"),
    path('limpiar/', clear_cart, name="CLS"),
]

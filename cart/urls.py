"""URLs for Cart App."""

from django.urls import path
from cart.views import store, add_product, remove_product, subtract_product, clear_cart

app_name = 'cart'

urlpatterns = [
    path('', store, name='store'),
    path('add/<int:product_id>/', add_product, name="add"),
    path('remove/<int:product_id>/', remove_product, name="remove"),
    path('subtract/<int:product_id>/', subtract_product, name="subtract"),
    path('clear/', clear_cart, name="clear"),
]

"""URLs for Cart App."""

from django.urls import path
from cart.views import store, add_product, remove_product, subtract_product, clear_cart

app_name = 'cart'

urlpatterns = [
    path('store/', store, name='store'),
    path('add_product/<int:product_id>/', add_product, name='add_product'),
    path('remove_product/<int:product_id>/',
         remove_product, name='remove_product'),
    path('subtract_product/<int:product_id>/',
         subtract_product, name='subtract_product'),
    path('clear_cart/', clear_cart, name='clear_cart'),
]

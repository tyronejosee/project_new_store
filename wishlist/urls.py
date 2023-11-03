"""URLs for Wishlist App."""

from django.urls import path
from wishlist.views import wishlist, add_product, remove_product, subtract_product

app_name = 'wishlist'

urlpatterns = [
    path('', wishlist, name='wishlist'),
    path('add_product/<int:product_id>/', add_product, name='add_product'),
    path('remove_product/<int:product_id>/',
         remove_product, name='remove_product'),
    path('subtract_product/<int:product_id>/',
         subtract_product, name='subtract_product'),
]

"""URLs for Wishlist App."""

from django.urls import path
from wishlist.views import wishlist, add_product, remove_product

app_name = 'wishlist'

urlpatterns = [
    path('', wishlist, name='wishlist'),
    path('add/<int:product_id>/', add_product, name="add"),
    path('remove/<int:product_id>/', remove_product, name="remove"),
]

"""URLs for Products App."""
from django.urls import path
from products.views import products_main

urlpatterns = [
    path("", products_main, name="products_main"),
]

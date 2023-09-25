"""URLs for Products App."""

from django.urls import path, include
from products.views import ProductListView, product_search


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("", ProductListView.as_view(), name="products_list"),
    path('product_search/', product_search, name='product_search'),
]

"""URLs for Products App."""

from django.urls import path, include
from products.views import ProductListView, ProductDetailView, product_search

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('catalog/', ProductListView.as_view(), name="products_list"),
    path('catalog/item-<int:pk>/',
         ProductDetailView.as_view(), name='product_detail'),
    path('find/', product_search, name='product_search'),
]

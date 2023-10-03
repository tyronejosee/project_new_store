"""URLs for Products App."""

from django.urls import path, include
from products.views import ProductListView, ProductDetailView, product_search

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('list/', ProductListView.as_view(), name="products_list"),
    path('list/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('browse/', product_search, name='product_search'),
]

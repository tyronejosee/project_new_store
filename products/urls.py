"""URLs for Products App."""

from django.urls import path, include
from products.views import (
    ProductListView, ProductDetailView, RecentProductsListView, product_search, CategoriesListView, BrandListView
)


urlpatterns = [
    # Others
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Public paths
    path('', product_search, name='product_search'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('items/', ProductListView.as_view(), name="products_list"),
    path('items/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('brands/<str:brand_name>/', BrandListView.as_view(), name='brand'),
    path('recent/', RecentProductsListView.as_view(), name="recent"),

    # Private paths
]

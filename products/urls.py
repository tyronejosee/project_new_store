"""URLs for Products App."""

from django.urls import path, include
from products.views import (
    ProductListView, ProductDetailView, RecentProductsListView, product_search, CategoriesListView, BrandFilterListView, CategoryFilterListView
)

app_name = 'products'

urlpatterns = [
    # Third-party URLs
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Products URLs
    path('', product_search, name='search'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('items/', ProductListView.as_view(), name='items'),
    path('items/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('category/<str:category_title>/', CategoryFilterListView.as_view(), name='category_filter'),
    path('brands/<str:brand_name>/', BrandFilterListView.as_view(), name='brand_filter'),
    path('recent/', RecentProductsListView.as_view(), name="recent"),
]

"""URLs for Products App."""

from django.urls import path, include
from products.views import (
    ProductListView, ProductDetailView, RecentProductsListView, product_search, CategoriesListView, BrandListView
)

app_name = 'products'

urlpatterns = [
    # Others
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Public paths
    path('', product_search, name='search'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('items/', ProductListView.as_view(), name='items'),
    path('items/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('brands/<str:brand_name>/', BrandListView.as_view(), name='brands'),
    path('recent/', RecentProductsListView.as_view(), name="recent"),
]

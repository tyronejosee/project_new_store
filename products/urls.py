"""URLs for Products App."""

from django.urls import path, include
from products.views import (
    ProductListView,
    ProductDetailView,
    RecentProductsListView,
    product_search,
    CategoriesListView,
    DealListView,
    DealDetailView,
    BrandFilterListView,
    CategoryFilterListView
)

app_name = 'products'

urlpatterns = [
    # Third-party URLs
    path('ckeditor/', include('ckeditor_uploader.urls')),

    # Products URLs
    path('', product_search, name='search'),
    path('', ProductListView.as_view(), name='prod_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('categories/<str:category_slug>/', CategoryFilterListView.as_view(), name='category_filter'),
    path('deals/', DealListView.as_view(), name='deal_list'),
    path('deals/<slug:slug>/', DealDetailView.as_view(), name='deal_detail'),
    path('brands/<str:brand_slug>/', BrandFilterListView.as_view(), name='brand_filter'),
    path('recent/', RecentProductsListView.as_view(), name="recent"),
]

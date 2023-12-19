"""URLs for Management App."""

from django.urls import path
from management.views import (
    ManagementView,
    PageListView,
    PageUpdateView,
    UserListView,
    ProductListView,
    DeactivatedProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductStatusToggleView,
    DealCreateView,
    DealListView,
    DealUpdateView,
    DealDeleteView
)

app_name = 'management'

urlpatterns = [
    path('dashboard/', ManagementView.as_view(), name='management'),
    path('pages/', PageListView.as_view(), name='page_list'),
    path('pages/update/<int:pk>', PageUpdateView.as_view(), name='page_update'),
    path('users/', UserListView.as_view(), name='user_list'),

    # Deals
    path('deals/create/', DealCreateView.as_view(), name='deal_create'),
    path('deals/read/', DealListView.as_view(), name='deal_list'),
    path('deals/update/<int:pk>', DealUpdateView.as_view(), name='deal_update'),
    path('deals/delete/<int:pk>', DealDeleteView.as_view(), name='deal_delete'),

    # Products
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/deactivated/', DeactivatedProductListView.as_view(), name='product_deactivated_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/deactivate/', ProductStatusToggleView.as_view(), {'action': 'deactivate'}, name='product_deactivate'),
    path('products/<int:pk>/activate/', ProductStatusToggleView.as_view(), {'action': 'activate'}, name='product_activate'),
]

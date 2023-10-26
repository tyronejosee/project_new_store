"""URLs for Management App."""

from django.urls import path
from management.views import (
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
)

app_name = 'management'

urlpatterns = [
    path('products/list/', ProductListView.as_view(), name='prod_list'),
    path('products/create/', ProductCreateView.as_view(), name='prod_create'),
    path('products/update/<int:pk>',
         ProductUpdateView.as_view(), name='prod_update'),
    path('products/delete/<int:pk>',
         ProductDeleteView.as_view(), name='prod_delete'),
]

"""URLs for Management App."""

from django.urls import path
from management.views import ProductListView

app_name = 'management'

urlpatterns = [
    path('products/list/', ProductListView.as_view(), name='product_list'),
]

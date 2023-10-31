"""URLs for Management App."""

from django.urls import path
from management.views import (
    ProductListView,
    DeletedProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductStatusToggleView
)

app_name = 'management'

urlpatterns = [
    path('products/available/', ProductListView.as_view(), name='prod_available'),
    path('products/deleted/', DeletedProductListView.as_view(),
         name='prod_deleted'),
    path('products/create/', ProductCreateView.as_view(), name='prod_create'),
    path('products/update/<int:pk>',
         ProductUpdateView.as_view(), name='prod_update'),
    path('products/<int:pk>/delete/', ProductStatusToggleView.as_view(),
         {'action': 'delete'}, name='prod_delete'),
    path('products/<int:pk>/reactivate/', ProductStatusToggleView.as_view(),
         {'action': 'reactivate'}, name='prod_reactivate'),
]

# path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='prod_delete'),

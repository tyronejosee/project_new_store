"""URLs for Home App."""

from django.urls import path
from home.views import PageDetailView, FeaturedProductListView

app_name = 'home'

urlpatterns = [
    path("", FeaturedProductListView.as_view(), name="featured_product"),
    path("company/<str:key>/", PageDetailView.as_view(), name="page_detail"),
]

"""URLs for Home App."""

from django.urls import path
from home.views import TermsAndConditionsView, AboutView, PrivacyView, FeaturedProductListView


urlpatterns = [
    path("", FeaturedProductListView.as_view(), name="featured_product"),
    path('terms-and-conditions/', TermsAndConditionsView.as_view(), name='terms'),
    path('about/', AboutView.as_view(), name='about'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
]

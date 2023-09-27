"""URLs for Home App."""

from django.urls import path
from home.views import landing_page, TermsAndConditionsView, AboutView, PrivacyView


urlpatterns = [
    path("", landing_page, name="landing_page"),
    path('terms-and-conditions/', TermsAndConditionsView.as_view(), name='terms'),
    path('about/', AboutView.as_view(), name='about'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
]

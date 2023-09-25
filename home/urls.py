"""URLs for Home App."""
from django.urls import path

from home.views import landing_page, TermsAndConditionsView, AboutView


urlpatterns = [
    path("", landing_page, name="landing_page"),
    path('terms-and-conditions/', TermsAndConditionsView.as_view(), name='terms'),
    path('about/', AboutView.as_view(), name='about'),
]

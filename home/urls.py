"""URL configuration for Home App."""
#from django.contrib import admin
from django.urls import path
from home.views import landing_page

urlpatterns = [
    path("", landing_page, name="landing_page"),
]

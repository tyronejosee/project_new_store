"""URLs for Accounts App."""
from django.urls import path
from accounts.views import accounts_main

urlpatterns = [
    path("", accounts_main, name="accounts_main"),
]

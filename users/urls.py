"""URLs for Products App."""

from django.urls import path
from users.views import Login

app_name = 'users'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
]

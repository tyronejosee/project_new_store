"""URLs for Users App."""

from django.urls import path
from users.views import UserProfileView, UserLoginView, UserRegistrationView

app_name = 'users'

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
]

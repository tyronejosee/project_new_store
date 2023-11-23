"""URLs for Users App."""

from django.urls import path
from users.views import UserRegistrationView, UserLoginView, user_logout

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
]

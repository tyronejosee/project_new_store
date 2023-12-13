"""URLs for Users App."""

from django.urls import path
from django.contrib.auth.views import PasswordResetDoneView
from users.views import (UserLoginView, user_logout, UserRegistrationView, PasswordChangeView)

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done', PasswordResetDoneView.as_view(), name='password_change_done'),
]

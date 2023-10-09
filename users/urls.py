"""URLs for Products App."""

from django.urls import path
from users.views import WelcomeView, SignUpView, ProfileUpdate, EmailUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
    path('welcome/', WelcomeView.as_view(), name="welcome"),
]

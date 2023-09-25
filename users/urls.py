from django.urls import path
from users.views import SignUpView, CustomUserUpdate, EmailUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', CustomUserUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
]

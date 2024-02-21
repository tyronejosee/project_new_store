"""Managers for Users App."""

from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """Manages CustomUser instances, including superusers."""

    def create_user(self, username, email, first_name, last_name, password):
        """Create a standard user."""
        if not email:
            raise ValueError("The user must have an email.")
        email = self.normalize_email(email)
        custom_user = self.model(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        custom_user.is_staff = False
        custom_user.set_password(password)
        custom_user.save()
        return custom_user

    def create_superuser(self, username, email, first_name, last_name, password):
        """Create a superuser or staff user."""
        custom_user = self.create_user(
            username, email, first_name, last_name, password)
        custom_user.is_superuser = True
        custom_user.is_staff = True
        custom_user.save()
        return custom_user

"""Models for Users App."""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Entity type model for CustomUser."""
    username = models.CharField("Username", max_length=100, unique=True)
    email = models.EmailField("Email", max_length=255, unique=True)
    first_name = models.CharField("First Name", max_length=255, blank=True)
    last_name = models.CharField("Last Name", max_length=255, blank=True)
    address = models.TextField("Address", blank=True)
    phone_number = models.CharField("Phone Number", max_length=15, blank=True)
    is_active = models.BooleanField("Is Active", default=True)
    is_staff = models.BooleanField("Is Staff", default=False)
    date_joined = models.DateTimeField("Date Joined", default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name"]

    class Meta:
        """Meta definition for CustomUser model."""
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}: {self.email}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_staff

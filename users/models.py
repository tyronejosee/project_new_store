"""Models for Users App."""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    """Class required by BaseAbstractUser."""

    def create_user(self, username, email, first_name, last_name, password=None):
        if not email:
            raise ValueError('The user must have an email.')

        custom_user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        custom_user.set_password(password)
        custom_user.save()
        return custom_user

    def create_superuser(self, username, email, first_name, last_name, password):
        custom_user = self.create_user(
            username=username,
            email,  # Pending
            first_name=first_name,
            last_name=last_name
        )

        custom_user.is_staff = True
        custom_user.save()
        return custom_user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Entity type model for CustomUser."""

    username = models.CharField(max_length=100, unique=True, verbose_name='Username')
    email = models.EmailField(max_length=254, unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='First Name')
    last_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Last Name')
    address = models.TextField(blank=True, verbose_name='Adress')
    phone_number = models.CharField(max_length=15, blank=True, verbose_name='Phone Number')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Date Joined')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    is_staff = models.BooleanField(default=False, verbose_name='Is Staff')

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.username}: {self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        """Property to check if the user is staff."""
        return self.is_staff

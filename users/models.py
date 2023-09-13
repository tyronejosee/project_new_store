"""Models for Users App."""
from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    """
    Model extending fields from the User class.
    """
    GENDER_CHOICES = [
    (1, 'Male'),
    (2, 'Female'),
    (3, 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=GENDER_CHOICES, default='', blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name='Address', blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name='City', blank=True, null=True)
    country = models.CharField(max_length=255, verbose_name='Country', blank=True, null=True)
    tax_number = models.CharField(max_length=50, verbose_name='Tax Number', blank=True, null=True)

    class Meta:
        """Adds extra metadata to the CustomUser model."""
        ordering = ['user__username']

"""Models for Users App."""
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class CustomUser(models.Model):
    """Model extending fields from the User class."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, verbose_name='Address', blank=True, null=True)
    city = models.CharField(max_length=255, verbose_name='City', blank=True, null=True)
    country = models.CharField(max_length=255, verbose_name='Country', blank=True, null=True)
    tax_number = models.CharField(max_length=50, verbose_name='Tax Number', blank=True, null=True)

    class Meta:
        """Adds extra metadata to the CustomUser model."""
        ordering = ['user__username']


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        CustomUser.objects.get_or_create(user=instance)

"""Models for Users App."""

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename


class Profile(models.Model):
    """Model extending fields from the User class."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        """Adds extra metadata to the Profile model."""
        ordering = ['user__username']


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    """Signal creates a User profile when a new User is saved."""
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)

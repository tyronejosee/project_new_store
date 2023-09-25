"""Models for Home App."""
from django.db import models


class Page(models.Model):
    """Entity type model for Pages."""

    CATEGORY_CHOICES = (
        ('terms', 'Terms & Conditions'),
        ('about', 'About'),
    )

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

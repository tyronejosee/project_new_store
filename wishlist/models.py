"""Models for Wishlist App."""

from django.db import models
from users.models import CustomUser


class Wishlist(models.Model):
    """Pending."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField('products.Product')

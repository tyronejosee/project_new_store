"""
Models for the Store App

This module contains the Django models used for representing products, categories,
currency types, images, and other entities in the store application.
"""

from django.db import models
from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator

class Category(models.Model):
    """
    Model representing a Category in the store.
    """
    category = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=250)
    show = models.BooleanField(default=True)

    def __str__(self):
        """
        Returns the name of the category as its string representation.
        """
        return str(self.category)

    class Meta:
        """
        Adds extra metadata to the Category model.
        """
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Image(models.Model):
    """
    Model representing a list of images in the products.
    """
    link = models.URLField()

    def __str__(self):
        """
        Returns the link of the image as its string representation.
        """
        return str(self.link)

    class Meta:
        """
        Adds extra metadata to the Image model.
        """
        verbose_name = "Image"
        verbose_name_plural = "Images"


class Currency(models.Model):
    """
    Model representing currency types in the store.
    """
    name = models.CharField(max_length=50, unique=True)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        """
        Returns the name of the currency as its string representation.
        """
        return str(self.name)

    class Meta:
        """
        Adds extra metadata to the currency model.
        """
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"


class Product(models.Model):
    """
    Model representing a product in the store.
    """
    date = models.DateTimeField(auto_now_add=True)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    detail = models.JSONField()
    show = models.BooleanField(default=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    admin_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        """
        Returns the name of the product as its string representation.
        """
        return str(self.title)

    class Meta:
        """
        Adds extra metadata to the Product model.
        """
        verbose_name = "Product"
        verbose_name_plural = "Products"

    @staticmethod
    @login_required
    def _get_admin_name_from_request():
        return request.user.username

    def save(self, *args, **kwargs):
        if self.admin_name is None:
            admin_name = self._get_admin_name_from_request()
            if admin_name:
                self.admin_name = admin_name
        super(Product, self).save(*args, **kwargs)

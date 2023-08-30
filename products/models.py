"""Models for Products App."""
from django.db import models


class Category(models.Model):
    """
    Model representing a Category in the store.
    """
    title = models.CharField(max_length=25, unique=True, verbose_name='Category')
    description = models.CharField(max_length=250, verbose_name='Description')
    show_hide = models.BooleanField(default=True, verbose_name='Show/Hide')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return str(self.title)

    class Meta:
        """
        Adds extra metadata to the Category model.
        """
        verbose_name_plural = "Categories"
        ordering = ['title']


class Product(models.Model):
    """
    Model representing a product in the store.
    """
    title = models.CharField(max_length=100, verbose_name='Title')
    stock = models.PositiveIntegerField(verbose_name='Stock')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Image')
    category = models.OneToOneField(Category, on_delete=models.CASCADE, verbose_name='Category')
    show_hide = models.BooleanField(default=True, verbose_name='Show/Hide')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return str(self.title)

    class Meta:
        """
        Adds extra metadata to the Product model.
        """
        verbose_name_plural = "Products"
        ordering = ['-updated_at', 'title']

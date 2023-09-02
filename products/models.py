"""Models for Products App."""
from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    """
    Catalog type model for Category.
    """
    title = models.CharField(max_length=25, unique=True, verbose_name='Category')
    description = RichTextField(max_length=250, blank=True, null=True, verbose_name='Description')
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


class Brand(models.Model):
    """
    Catalog type model for Brand.
    """
    name = models.CharField(max_length=50, unique=True, verbose_name='Name')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return str(self.name)

    class Meta:
        """
        Adds extra metadata to the Brand model.
        """
        verbose_name_plural = "Brands"
        ordering = ['name']


class Product(models.Model):
    """
    Entity type model for Products.
    """
    WARRANTY_CHOICES = [
    (1, '1 month'),
    (3, '3 months'),
    (6, '6 months'),
    (12, '1 year'),
    (24, '2 years'),
    ]

    title = models.CharField(max_length=100, verbose_name='Title')
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE, verbose_name='Brand')
    category = models.OneToOneField(Category, on_delete=models.CASCADE, verbose_name='Category')
    image = models.ImageField(upload_to='products/', verbose_name='Image')
    description = RichTextField(verbose_name='Description')
    specifications = RichTextField(verbose_name='Specifications')
    stock = models.PositiveIntegerField(verbose_name='Stock')
    normal_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discount_end_date = models.DateField(blank=True, null=True)
    warranty = models.IntegerField(choices=WARRANTY_CHOICES, default='12')
    featured = models.BooleanField(default=False, verbose_name='Featured')
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

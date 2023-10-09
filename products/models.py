"""Models for Products App."""

from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    """Catalog type model for Category."""

    SECTION_CHOICES = [
        (1, 'pending'),
        (2, 'Electronic Deals'),
        (3, 'TVs & Home Theater'),
        (4, 'Cell Phones'),
        (5, 'Computers & Office'),
        (6, 'Kids Electronics'),
        (7, 'Headphones'),
        (8, 'Cameras'),
        (9, 'Speakers & Audio Systems'),
        (10, 'Tablets & E-Readers'),
        (11, 'Wearable Technology'),
        (12, 'Wi-Fi & Networking'),
    ]

    title = models.CharField(max_length=50, unique=True, verbose_name='Category')
    section = models.IntegerField(choices=SECTION_CHOICES, default='1')
    show_hide = models.BooleanField(default=True, verbose_name='Show/Hide')

    class Meta:
        """Adds extra metadata to the Category model."""
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return str(self.title)


class Brand(models.Model):
    """Catalog type model for Brand."""

    name = models.CharField(max_length=50, unique=True, verbose_name='Name')
    show_hide = models.BooleanField(default=True, verbose_name='Show/Hide')

    class Meta:
        """Adds extra metadata to the Brand model."""
        verbose_name_plural = "Brands"
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    """Entity type model for Products."""

    WARRANTY_CHOICES = [
        (1, '1 month'),
        (3, '3 months'),
        (6, '6 months'),
        (12, '1 year'),
        (24, '2 years'),
        (36, '3 years'),
    ]

    title = models.CharField(max_length=255, verbose_name='Title')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Brand')
    normal_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    image = models.ImageField(upload_to='products/', verbose_name='Image')
    stock = models.PositiveIntegerField(default=100, blank=True, null=True, verbose_name='Stock')
    warranty = models.IntegerField(choices=WARRANTY_CHOICES, default='12', blank=True, null=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discount_end_date = models.DateField(blank=True, null=True)
    featured = models.BooleanField(default=False, verbose_name='Featured')
    show_hide = models.BooleanField(default=True, verbose_name='Show/Hide')
    description = RichTextField(blank=True, null=True, verbose_name='Description')
    specifications = RichTextField(blank=True, null=True, verbose_name='Specifications')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        """Adds extra metadata to the Product model."""
        verbose_name_plural = "Products"
        ordering = ['-created_at', 'title']

    def __str__(self):
        return str(self.title)

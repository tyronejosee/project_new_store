"""Models for Products App."""

import os
from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    """Catalog type model for Category."""

    title = models.CharField(max_length=50, unique=True, verbose_name='Category')
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name='Slug')
    show_hide = models.BooleanField(default=True, verbose_name='Show/Hide')

    class Meta:
        """Meta definition for Category."""
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return str(self.title)
    
    def save(self, *args, **kwargs):
        """Override method to save a slug if not existing or different from the title."""
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Brand(models.Model):
    """Catalog type model for Brand."""

    name = models.CharField(max_length=50, unique=True, verbose_name='Name')
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name='Slug')
    show_hide = models.BooleanField(default=True, verbose_name='Show/Hide')

    class Meta:
        """Meta definition for Brands."""
        verbose_name_plural = "Brands"
        ordering = ['name']

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        """Override method to save a slug if not existing or different from the name."""
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Deal(models.Model):
    """Entity type model for Deals."""

    name = models.CharField(max_length=50, unique=True, verbose_name='Name')
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name='Slug')
    image = models.ImageField(upload_to='deals/', blank=True, null=True, verbose_name='Image')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Discount')
    start_date = models.DateField(blank=True, null=True, verbose_name='Start Date')
    end_date = models.DateField(blank=True, null=True, verbose_name='End Date')
    status = models.BooleanField(default=True, verbose_name='Status')

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        """Override method to save a slug if not existing or different from the name."""
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


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
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True, verbose_name='Slug')
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, verbose_name='Brand')
    normal_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Price')
    deal = models.ForeignKey(
        Deal, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Deal')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Category')
    image = models.ImageField(
        upload_to='products/', blank=True, null=True, verbose_name='Image')
    stock = models.PositiveIntegerField(default=100, verbose_name='Stock')
    warranty = models.IntegerField(
        choices=WARRANTY_CHOICES, default='12', blank=True, null=True)
    featured = models.BooleanField(default=False, verbose_name='Featured')
    show_hide = models.BooleanField(default=True, verbose_name='Show/Hide')
    description = RichTextField(
        blank=True, null=True, verbose_name='Description')
    specifications = RichTextField(
        blank=True, null=True, verbose_name='Specifications')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    class Meta:
        """Meta definition for Product."""
        verbose_name_plural = "Products"
        ordering = ['-created_at', 'title']

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        """Override the method to rename the image and save a slug."""
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)

        if self.image and self.image.name:
            if not self.pk or self._state.adding or self.image != self.__class__.objects.get(pk=self.pk).image:
                file_name, file_extension = os.path.splitext(self.image.name)   # Gets the original file name
                title_in_lowercase = self.title.lower()    # Create a new name in lowercase
                new_file_name = f'item-{title_in_lowercase}{file_extension}'
                self.image.name = new_file_name    # Changes the file name

        super(Product, self).save(*args, **kwargs)

    def price_with_discount(self):
        """Method applies a discount with a percentage to the normal_price of a product."""
        if self.deal:
            return self.normal_price - (self.normal_price * (self.deal.discount / 100))
        return self.normal_price


@receiver(models.signals.post_delete, sender=Product)
def auto_remove_image(sender, instance, **kwargs):
    """Signal to remove the related image when deleting a product."""
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

"""Models for Products App."""

import os
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from utils.validators import validate_extension


class Category(models.Model):
    """Catalog type model for Category."""
    title = models.CharField(max_length=50, unique=True, verbose_name="Category")
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name="Slug")
    show_hide = models.BooleanField(default=True, verbose_name="Show/Hide")

    class Meta:
        """Meta definition for Category."""
        verbose_name_plural = "Categories"
        ordering = ["title"]

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        # Create a slug based on the title
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Brand(models.Model):
    """Catalog type model for Brand."""
    name = models.CharField(max_length=50, unique=True, verbose_name="Name")
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name="Slug")
    show_hide = models.BooleanField(default=True, verbose_name="Show/Hide")

    class Meta:
        """Meta definition for Brands."""
        verbose_name_plural = "Brands"
        ordering = ["name"]

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        # Create a slug based on the name
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Deal(models.Model):
    """Entity type model for Deals."""
    name = models.CharField(max_length=50, unique=True, verbose_name="Name")
    slug = models.SlugField(unique=True, null=True, blank=True, verbose_name="Slug")
    image = models.ImageField(upload_to="deals/", blank=True, null=True, verbose_name="Image")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Discount")
    start_date = models.DateField(blank=True, null=True, verbose_name="Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    status = models.BooleanField(default=True, verbose_name="Status")

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        # Create a slug based on the name
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)

        # Rename the image associated with the deal
        if self.image and self.image.name:
            if not self.pk or self._state.adding or self.image != self.__class__.objects.get(pk=self.pk).image:
                file_name, file_extension = os.path.splitext(self.image.name)
                title = self.slug[:100]
                file_name = f"{title}{file_extension}"
                self.image.name = file_name
        super(Deal, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Method returns the canonical URL for the details of an deal."""
        return reverse("deal_detail", kwargs={"slug": self.slug})


class Product(models.Model):
    """Entity type model for Products."""
    WARRANTY_CHOICES = [
        (1, "1 month"),
        (3, "3 months"),
        (6, "6 months"),
        (12, "1 year"),
        (24, "2 years"),
        (36, "3 years"),
    ]
    title = models.CharField(max_length=255, verbose_name="Title")
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True, verbose_name="Slug")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Brand")
    normal_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Sale Price")
    deal = models.ForeignKey(Deal, on_delete=models.SET_NULL, null=True, blank=True, related_name="products", verbose_name="Deal")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Category")
    image = models.ImageField(upload_to="products/", validators=[validate_extension], blank=True, null=True, verbose_name="Image")
    stock = models.PositiveIntegerField(default=100, verbose_name="Stock")
    warranty = models.IntegerField(choices=WARRANTY_CHOICES, default="12", blank=True, null=True)
    featured = models.BooleanField(default=False, verbose_name="Featured")
    show_hide = models.BooleanField(default=True, verbose_name="Show/Hide")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    specifications = models.TextField(blank=True, null=True, verbose_name="Specifications")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        """Meta definition for Product."""
        verbose_name_plural = "Products"
        ordering = ["-created_at", "title"]

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        # Apply method on the price when saving a product
        self.update_sale_price()

        # Create a slug based on the title
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)

        # Rename the image associated with the product
        if self.image and self.image.name:
            if not self.pk or self._state.adding or self.image != self.__class__.objects.get(pk=self.pk).image:
                file_name, file_extension = os.path.splitext(self.image.name)
                title = self.slug[:100]
                file_name = f"{title}{file_extension}"
                self.image.name = file_name

        super(Product, self).save(*args, **kwargs)

    def update_sale_price(self):
        """Method update sale_price based on deal and deal dates."""
        # Check if there is a deal on the product and if it has a discount
        if self.deal and self.deal.discount is not None:
            if self.deal.start_date and self.deal.end_date:
                current_date = timezone.now().date() # Today
                # Apply the discount and save the "sale_price"
                if self.deal.start_date <= current_date <= self.deal.end_date:
                    self.sale_price = self.normal_price - (self.normal_price * (self.deal.discount / 100))
                else:
                    self.sale_price = None
            else:
                self.sale_price = None
        else:
            self.sale_price = None
        # If no conditions are met, set "None" for the "sale_price"

    def is_new(self):
        """Method returns True if the product is new, created, or updated within a day."""
        return (
            self.created_at >= timezone.now() - timezone.timedelta(days=1) or
            self.updated_at >= timezone.now() - timezone.timedelta(days=1)
        )


# Signals

@receiver(post_save, sender=Deal)
@receiver(post_delete, sender=Deal)
def product_update_sale_prices(sender, instance, **kwargs):
    """Signal handler to update sale_prices when a Deal is saved or deleted."""
    products = Product.objects.filter(deal=instance)

    # Iterate through the products and update the "sale_price"
    for product in products:
        product.update_sale_price()
        product.save()


@receiver(post_delete, sender=Product)
def product_remove_image(sender, instance, **kwargs):
    """Signal to remove the related image when deleting a product."""
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(post_delete, sender=Deal)
def deal_remove_image(sender, instance, **kwargs):
    """Signal to remove the related image when deleting a deal."""
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

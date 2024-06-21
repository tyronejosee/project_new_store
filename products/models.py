"""Models for Products App."""

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from cloudinary.models import CloudinaryField
from products.choices import WARRANTY_CHOICES


class Category(models.Model):
    """Catalog type model for Category."""

    title = models.CharField("Category", max_length=50, unique=True)
    slug = models.SlugField(
        "Slug",
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    show_hide = models.BooleanField("Show/Hide", default=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "category"
        verbose_name_plural = "categories"
        app_label = "products"

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        # Create a slug based on the title
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Brand(models.Model):
    """Catalog type model for Brand."""

    name = models.CharField("Name", max_length=255, unique=True)
    slug = models.SlugField(
        "Slug",
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    show_hide = models.BooleanField("Show/Hide", default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "brand"
        verbose_name_plural = "brands"
        app_label = "products"

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        # Create a slug based on the name
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Deal(models.Model):
    """Entity type model for Deals."""

    name = models.CharField("Name", max_length=255, unique=True)
    slug = models.SlugField(
        "Slug",
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    image = CloudinaryField("Image")
    description = models.TextField("Description", blank=True, null=True)
    discount = models.DecimalField(
        "Discount", max_digits=5, decimal_places=2, blank=True, null=True
    )
    start_date = models.DateField("Start Date", blank=True, null=True)
    end_date = models.DateField("End Date", blank=True, null=True)
    status = models.BooleanField("Status", default=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Deal"
        verbose_name_plural = "deals"
        app_label = "products"

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        # Create a slug based on the name
        if not self.slug or self.slug != slugify(self.name):
            self.slug = slugify(self.name)
        super(Deal, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Method returns the canonical URL for the details of an deal."""
        return reverse("deal_detail", kwargs={"slug": self.slug})


class Product(models.Model):
    """Entity type model for Products."""

    title = models.CharField("Title", max_length=255, unique=True)
    slug = models.SlugField(
        "Slug",
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Brand",
    )
    normal_price = models.DecimalField(
        "Price",
        max_digits=10,
        decimal_places=2,
    )
    sale_price = models.DecimalField(
        "Sale Price", max_digits=10, decimal_places=2, null=True, blank=True
    )
    deal = models.ForeignKey(
        Deal,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
        verbose_name="Deal",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Category",
    )
    image = CloudinaryField("Image")
    stock = models.PositiveIntegerField("Stock", default=100)
    warranty = models.IntegerField(
        "Warranty", choices=WARRANTY_CHOICES, default="12", blank=True
    )
    featured = models.BooleanField("Featured", default=False)
    show_hide = models.BooleanField("Show/Hide", default=True)
    description = models.TextField("Description", blank=True, null=True)
    specifications = models.TextField("Specifications", blank=True, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "product"
        verbose_name_plural = "products"
        app_label = "products"

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.update_sale_price()

        # Create a slug based on the title
        if not self.slug or self.slug != slugify(self.title):
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def update_sale_price(self):
        """Method update sale_price based on deal and deal dates."""
        # Check if there is a deal on the product and if it has a discount
        if self.deal and self.deal.discount is not None:
            if self.deal.start_date and self.deal.end_date:
                current_date = timezone.now().date()  # Today
                # Apply the discount and save the "sale_price"
                if self.deal.start_date <= current_date <= self.deal.end_date:
                    self.sale_price = self.normal_price - (
                        self.normal_price * (self.deal.discount / 100)
                    )
                else:
                    self.sale_price = None
            else:
                self.sale_price = None
        else:
            self.sale_price = None
        # If no conditions are met, set "None" for the "sale_price"

    def is_new(self):
        """Returns True if the product is new."""
        return self.created_at >= timezone.now() - timezone.timedelta(
            days=1
        ) or self.updated_at >= timezone.now() - timezone.timedelta(days=1)


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

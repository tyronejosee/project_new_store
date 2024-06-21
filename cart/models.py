"""Models for Cart App."""

from django.db import models
from users.models import CustomUser
from products.models import Product


class Cart(models.Model):
    """Model definition for Cart."""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        ordering = ["user"]
        verbose_name = "cart"
        verbose_name_plural = "cart"
        app_label = "cart"

    def __str__(self):
        return str(f"Cart of {self.user.username}")

    def clear_cart(self):
        self.cart_items.all().delete()


class CartItem(models.Model):
    """Model definition for CartItem."""

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="cart_items",
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["cart"]
        verbose_name = "cart item"
        verbose_name_plural = "cart items"
        app_label = "cart"

    def __str__(self):
        return f"{self.cart.user} - {self.quantity}"

    def add_to_cart(self, quantity=1):
        self.quantity += quantity
        self.save()

    def remove_from_cart(self):
        self.delete()

    def subtract_from_cart(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.save()
        else:
            self.remove_from_cart()

    def total_price(self):
        """Calculate the total price for this item."""
        return self.product.normal_price * self.quantity


class Wishlist(models.Model):
    """Model definition for Wishlist."""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ["user"]
        verbose_name = "wishlist"
        verbose_name_plural = "wishlist"
        app_label = "cart"

    def __str__(self):
        total_products = self.products.count()
        return f"{self.user.username} ({total_products} prods)"

    def add_product(self, product):
        self.products.add(product)

    def remove_product(self, product):
        self.products.remove(product)

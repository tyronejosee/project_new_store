"""Models for Cart App."""

from django.db import models
from users.models import CustomUser
from products.models import Product


class Cart(models.Model):
    """Pivot type model for Cart."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        total_products = self.products.count()
        return f'{self.user.username} ({total_products} prods)'

    def add_product(self, product):
        """Add a product to the cart."""
        self.products.add(product)

    def remove_product(self, product):
        """Remove a product from the cart."""
        self.products.remove(product)

    def subtract_product(self, product):
        """Subtract a product from the cart."""
        if product in self.products.all():
            self.products.remove(product)

    def clear_cart(self):
        """Clear the cart."""
        self.products.clear()

    def total_price(self):
        """Calculate the total price of all products in the cart."""
        total_price = sum(product.normal_price for product in self.products.all())
        return total_price


class Wishlist(models.Model):
    """Pivot type model for Wishlist."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        total_products = self.products.count()
        return f'{self.user.username} ({total_products} prods)'

    def add_product(self, product):
        """Add a product to the Wishlist."""
        self.products.add(product)

    def remove_product(self, product):
        """Remove a product from the Wishlist."""
        self.products.remove(product)

    def subtract_product(self, product):
        """Subtract a product from the Wishlist."""
        if product in self.products.all():
            self.products.remove(product)

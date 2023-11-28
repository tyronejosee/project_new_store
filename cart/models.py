"""Models for Cart App."""

from django.db import models
from users.models import CustomUser
from products.models import Product

# TODO: Add shipping fields, Delete data from Custom User

class Cart(models.Model):
    """Pivot type model for Cart."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'Cart of {self.user.username}'


class CartItem(models.Model):
    """Pivot type model for CartItem."""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.cart.user} - {self.quantity}'

    def add_to_cart(self, quantity=1):
        """Add this item to the cart with a specified quantity."""
        self.quantity += quantity
        self.save()

    def remove_from_cart(self):
        """Remove this item from the cart."""
        self.delete()

    def subtract_from_cart(self):
        """Subtract one unit of this item from the cart."""
        if self.quantity > 1:
            self.quantity -= 1
            self.save()
        else:
            self.remove_from_cart()

    def total_price(self):
        """Calculate the total price for this item."""
        return self.product.normal_price * self.quantity


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

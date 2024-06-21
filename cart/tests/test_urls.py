"""URLs Tests for Cart App."""

from django.urls import reverse, resolve

from utils.tests import BaseTestCase
from cart.views import (
    cart,
    add_prod_cart,
    remove_prod_cart,
    subtract_prod_cart,
    clear_cart,
    add_prod_wishlist,
    remove_prod_wishlist,
)


class CartUrlsTest(BaseTestCase):
    """Tests for Cart urls."""

    def test_cart_url(self):
        """Test resolves cart URL and view."""
        url = reverse("cart:cart")
        resolver = resolve(url)
        self.assertEqual(resolver.func, cart)

    def test_add_prod_cart_url(self):
        """Test resolves add_prod_cart URL and view."""
        url = reverse("cart:add_prod_cart", args=[self.product.id])
        resolver = resolve(url)
        self.assertEqual(resolver.func, add_prod_cart)

    def test_remove_prod_cart_url(self):
        """Test resolves remove_prod_cart URL and view."""
        url = reverse("cart:remove_prod_cart", args=[self.product.id])
        resolver = resolve(url)
        self.assertEqual(resolver.func, remove_prod_cart)

    def test_subtract_prod_cart_url(self):
        """Test resolves subtract_prod_cart URL and view."""
        url = reverse("cart:subtract_prod_cart", args=[self.product.id])
        resolver = resolve(url)
        self.assertEqual(resolver.func, subtract_prod_cart)

    def test_clear_cart_url(self):
        """Test resolves clear_cart URL and view."""
        url = reverse("cart:clear_cart")
        resolver = resolve(url)
        self.assertEqual(resolver.func, clear_cart)


class WishlistUrlsTest(BaseTestCase):
    """Tests for Wishlist urls."""

    def test_add_prod_wishlist_url(self):
        """Test resolves add_prod_wishlist URL and view."""
        url = reverse("cart:add_prod_wishlist", args=[self.product.id])
        resolver = resolve(url)
        self.assertEqual(resolver.func, add_prod_wishlist)

    def test_remove_prod_wishlist_url(self):
        """Test resolves remove_prod_wishlist URL and view."""
        url = reverse("cart:remove_prod_wishlist", args=[self.product.id])
        resolver = resolve(url)
        self.assertEqual(resolver.func, remove_prod_wishlist)

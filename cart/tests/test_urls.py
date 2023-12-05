"""URLs Tests for the Cart App."""

from django.urls import reverse, resolve
from cart.tests.test_base import BaseTestCase
from cart.views import (
    cart,
    add_prod_cart,
    remove_prod_cart,
    subtract_prod_cart,
    clear_cart,
    add_prod_wishlist,
    remove_prod_wishlist
)


class RoutingCartTest(BaseTestCase):
    """Tests for the proper functioning of cart routes."""

    def test_url_cart(self):
        """Verifies resolution for cart view, ex:'/cart/'."""
        url = reverse('cart:cart')
        resolver = resolve(url)
        self.assertEqual(resolver.func, cart)

    def test_url_add_prod_cart(self):
        """Verifies resolution for add_prod_cart view, ex:'/cart/add/123'."""
        url = reverse('cart:add_prod_cart', args=[self.product.id])
        resolver = resolve(url)
        self.assertEqual(resolver.func, add_prod_cart)

    def test_url_remove_prod_cart(self):
        """Verifies resolution for remove_prod_cart view, ex:'/cart/remove/123'."""
        url = reverse('cart:remove_prod_cart', args=[self.product.id])
        resolver = resolve(url)
        self.assertEqual(resolver.func, remove_prod_cart)

    def test_url_subtract_prod_cart(self):
        """Verifies resolution for subtract_prod_cart view, ex:'/cart/subtract/123'."""
        url = reverse('cart:subtract_prod_cart', args=[self.product.id])
        resolver = resolve(url)
        self.assertEqual(resolver.func, subtract_prod_cart)

    def test_url_clear_cart(self):
        """Verifies resolution for clear_cart view, ex:'/cart/clear/'."""
        url = reverse('cart:clear_cart')
        resolver = resolve(url)
        self.assertEqual(resolver.func, clear_cart)


class RoutingWishlistTest(BaseTestCase):
    """Tests for the proper functioning of wishlist routes."""

    def test_url_add_prod_wishlist(self):
        """Verifies resolution for add_prod_wishlist view, ex:'/wishlist/add/123'."""
        url = reverse('cart:add_prod_wishlist', args=[self.product.id])
        resolver = resolve(url)
        self.assertEqual(resolver.func, add_prod_wishlist)

    def test_url_remove_prod_wishlist(self):
        """Verifies resolution for remove_prod_wishlist view, ex:'/wishlist/remove/123'."""
        url = reverse('cart:remove_prod_wishlist', args=[self.product.id])
        resolver = resolve(url)
        self.assertEqual(resolver.func, remove_prod_wishlist)

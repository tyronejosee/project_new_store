"""Tests for Cart App."""

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

    # Urls
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

    """
    TODO: FIX ERROR
    def test_url_remove_prod_cart(self):
        # Verifies resolution for remove_prod_cart view, ex:'/cart/remove/123'.
        url = reverse('cart:remove_prod_cart', args=[self.product.id])
        resolver = resolve(url)
        self.assertEqual(resolver.func, remove_prod_cart)
    """

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

    # Status code
    def test_status_code_cart(self):
        """Verifies status code when adding a product to the cart."""
        url = reverse('cart:cart')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_status_code_add_prod_cart(self):
        """Verify status code when adding a product."""
        url = reverse('cart:add_prod_cart', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    """
    TODO: FIX ERROR
    def test_status_code_remove_prod_cart(self):
        # Verify status code when remove a product.
        url = reverse('cart:remove_prod_cart', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
    """

    """
    TODO: Fix error
    def test_status_code_subtract_prod_cart(self):
        # Verify status code when subtract a product.
        url = reverse('cart:subtract_prod_cart', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
    """

    """
    TODO: FIX ERROR
    def test_status_code_clear_cart(self):
        # Verify status code when clear cart.
        url = reverse('cart:clear_cart')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
    """

class RoutingWishlistTest(BaseTestCase):
    """Tests for the proper functioning of wishlist routes."""

    # Urls
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

    # Status code
    def test_status_code_add_prod_wishlist(self):
        """Verify status code when adding a product."""
        url = reverse('cart:add_prod_wishlist', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_status_code_remove_prod_wishlist(self):
        """Verify status code when remove a product."""
        url = reverse('cart:remove_prod_wishlist', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

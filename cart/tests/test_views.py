"""Tests for Cart App."""

from cart.tests.test_base import BaseTestCase


class TestCartView(BaseTestCase):
    """Tests for cart and wishlist views."""

    """ TODO: Fix fails
    def test_cart_view_auth_user(self):
        """Tests for the cart when the user is authenticated."""
        # Make a request to cart
        response = self.client.get('/cart/')

        # Check the contexts
        self.assertIn('cart', response.context)
        self.assertIn('cart_products', response.context)
        self.assertIn('cart_count', response.context)
        self.assertIn('wishlist', response.context)
        self.assertIn('wishlist_products', response.context)
        self.assertIn('wishlist_count', response.context)

        # Check if the template is correct
        self.assertTemplateUsed(response, 'cart/cart.html')
    """

    def test_cart_view_unauth_user(self):
        """Tests for the cart when the user is not authenticated."""
        # Log out the user
        self.client.logout()
        # Make a request to cart
        response = self.client.get('/cart/')
        # Redirects to login
        self.assertRedirects(response, '/users/login/?next=/cart/')

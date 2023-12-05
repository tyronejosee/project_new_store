"""Views Tests for the Payment App."""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from products.models import Product


class PaymentViewsTest(TestCase):
    """Tests for payment views."""

    def setUp(self):
        # Create a default user
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass',
            first_name='Test',
            last_name='User'
        )
        # Log in the user created
        self.client.login(username='testuser', password='testpass')
        # Create a product
        self.product = Product.objects.create(title='Test Product', normal_price=10)

    """
    def test_check_out_view(self):
        # Verifies the functionality of the 'checkout' view
        response = self.client.get(reverse(
            'payment:checkout', kwargs={'product_id': self.product.id})
        )
        # Expected responses
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product'], self.product)
        self.assertIsNotNone(response.context['paypal'])
    """

    def test_payment_success_view(self):
        """Verifies the functionality of the 'payment_success' view."""
        response = self.client.get(reverse(
            'payment:payment_success', kwargs={'product_id': self.product.id})
        )
        # Expected responses
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product'], self.product)

    def test_payment_failed_view(self):
        """Verifies the functionality of the 'payment_failed' view."""
        response = self.client.get(reverse(
            'payment:payment_failed', kwargs={'product_id': self.product.id})
        )
        # Expected responses
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product'], self.product)

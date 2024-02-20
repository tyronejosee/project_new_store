"""URLs Tests for Payment App."""

from django.urls import resolve, reverse
from utils.tests import BaseTestCase
from payment.views import check_out, payment_success, payment_failed


class PaymentUrlsTest(BaseTestCase):
    """Tests for Payment URLs."""

    def test_checkout_url(self):
        """"Test Resolves checkout URL and view."""
        url = reverse("payment:checkout", args=[self.product.id])
        resolver = resolve(url)
        self.assertEqual(resolver.func, check_out)

    def test_payment_success_url(self):
        """"Test Resolves payment_success URL and view."""
        url = reverse("payment:payment_success", args=[self.product.id])
        response = self.client.get(url)
        resolver = resolve(url)
        self.assertEqual(resolver.func, payment_success)
        self.assertEqual(response.status_code, 200)

    def test_payment_failed_url(self):
        """"Test Resolves payment_failed URL and view."""
        url = reverse("payment:payment_failed", args=[self.product.id])
        response = self.client.get(url)
        resolver = resolve(url)
        self.assertEqual(resolver.func, payment_failed)
        self.assertEqual(response.status_code, 200)

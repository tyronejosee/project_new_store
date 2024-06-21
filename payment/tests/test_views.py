"""Views Tests for Payment App."""

from django.urls import reverse

from utils.tests import BaseTestCase


class PaymentViewsTest(BaseTestCase):
    """Tests for Payment views."""

    def test_payment_success_view(self):
        """Verifies the functionality of the payment_success view."""
        url = reverse(
            "payment:payment_success",
            kwargs={"product_id": self.product.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["product"], self.product)

    def test_payment_failed_view(self):
        """Verifies the functionality of the payment_failed view."""
        url = reverse(
            "payment:payment_failed",
            kwargs={"product_id": self.product.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["product"], self.product)

"""Test Base for Cart App."""

from django.test import TestCase
from django.contrib.auth import get_user_model
from products.models import Product, Brand, Category, Deal


class BaseTestCase(TestCase):
    """Base test case for common setup in test classes."""

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

        # Create a product with its foreign key objects
        category = Category.objects.create(title='Test Category')
        brand = Brand.objects.create(name='Test Brand')
        deal = Deal.objects.create(name='Test Deal')

        self.product = Product.objects.create(
            title='Test Product',
            brand=brand,
            normal_price=10.0,
            deal=deal,
            category=category,
            stock=100,
            warranty=12,
            featured=False,
            show_hide=True,
            description='Test description',
            specifications='Test specifications'
        )

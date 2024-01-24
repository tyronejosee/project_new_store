"""Utils: Test Base."""

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from products.models import Product, Brand, Category, Deal
from home.models import Page


class BaseTestCase(TestCase):
    """Base test case for common setup in test classes."""

    def setUp(self):
        super().setUp()
        self.client = Client()

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

        
        # Foreign key for product
        category = Category.objects.create(title='Test Category')
        brand = Brand.objects.create(name='Test Brand')
        deal = Deal.objects.create(name='Test Deal')

        # Create a product
        self.product = Product.objects.create(
            title='Test Product',
            brand=brand,
            normal_price=10.0,
            deal=deal,
            category=category,
            image=None,
            stock=100,
            warranty=12,
            featured=False,
            show_hide=True,
            description='Test description',
            specifications='Test specifications'
        )

        # Home pages
        self.page = Page.objects.create(
            key='page_example',
            content='Content Example'
        )

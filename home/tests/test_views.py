"""Views Tests for the Home App."""

from decimal import Decimal
from django.test import TestCase, Client
from django.urls import reverse
from home.models import Page
from products.models import Product, Brand, Deal, Category


class HomeViewsTest(TestCase):
    """Test cases for the views in the Home app."""
    def setUp(self):
        brand = Brand.objects.create(name='Brand Example')
        deal = Deal.objects.create(name='Deal Example', discount=10)
        category = Category.objects.create(title='Category Example')

        self.product1 = Product.objects.create(
            title='Product Example',
            show_hide=True,
            stock=5,
            normal_price=Decimal('100.00'),
            brand=brand,
            deal=deal,
            category=category
        )

        self.page1 = Page.objects.create(
            key='page_example',
            content='Content Example'
        )

        self.client = Client()

    def test_index_view(self):
        """Test for IndexTemplateView."""
        url = reverse('home:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertContains(response, self.product1.title)

    def test_page_detail_view(self):
        """Test for PageDetailView."""
        url = reverse('home:page_detail', kwargs={'key': self.page1.key})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/page_detail.html')
        self.assertEqual(response.context_data['page'], self.page1)
        self.assertContains(response, self.page1.content)

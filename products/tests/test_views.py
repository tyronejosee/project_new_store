"""Views Tests for Product App."""

from django.test import TestCase, Client
from django.urls import reverse

from products.models import Product, Brand, Deal, Category


class ProductViewsTest(TestCase):
    """Tests for Products views."""

    def setUp(self):
        """Set up test data."""
        self.brand = Brand.objects.create(name="Test Brand")
        self.deal = Deal.objects.create(name="Test Deal", discount=10)
        self.category = Category.objects.create(title="Test Category")

        self.product = Product.objects.create(
            title="Test Product",
            normal_price=50.99,
            brand=self.brand,
            deal=self.deal,
            category=self.category,
            image=None,
            stock=10,
            show_hide=True,
        )

        self.client = Client()

    def test_product_list_view(self):
        """Test for ProductListView."""
        url = reverse("products:prod_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_list.html")
        self.assertContains(response, "All Products")

    def test_product_detail_view(self):
        """Test for ProductDetailView."""
        url = reverse("products:detail", args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")
        self.assertContains(response, "Test Product")

    def test_categories_list_view(self):
        """Test for CategoriesListView."""
        url = reverse("products:categories")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_list.html")
        self.assertContains(response, "Categories")

    def test_deal_list_view(self):
        """Test for DealListView."""
        url = reverse("products:deal_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/deal_list.html")

    def test_deal_detail_view(self):
        """Test for DealDetailView."""
        url = reverse("products:deal_detail", args=[self.deal.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/deal_detail.html")
        self.assertContains(response, "Test Deal")

    def test_recent_products_list_view(self):
        """Test for RecentProductsListView."""
        url = reverse("products:recent")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_list.html")
        self.assertContains(response, "Recent Products")

    def test_category_filter_list_view(self):
        """Test for CategoryFilterListView."""
        url = reverse("products:category_filter", args=[self.category.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_list.html")
        self.assertContains(response, "Test Category")

    def test_brand_filter_list_view(self):
        """Test for BrandFilterListView."""
        url = reverse("products:brand_filter", args=[self.brand.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_list.html")
        self.assertContains(response, "Test Brand")

    def test_product_search_view(self):
        """Test for product_search."""
        url = reverse("products:search")
        response = self.client.get(url, {"search": "Test"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_list.html")
        self.assertContains(response, "Test Product")

    def test_product_search_view_empty_query(self):
        """Test for product_search with empty query."""
        url = reverse("products:search")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_list.html")

    def test_product_search_view_with_results(self):
        """Test for product_search with results."""
        url = reverse("products:search")
        response = self.client.get(url, {"search": "Test"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_list.html")
        self.assertContains(response, "Test Product")

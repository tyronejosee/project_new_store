"""URLs Tests for the Product App."""

from django.test import TestCase
from django.urls import reverse, resolve
from products.views import (
    product_search,
    ProductListView,
    ProductDetailView,
    CategoriesListView,
    CategoryFilterListView,
    DealListView,
    DealDetailView,
    BrandFilterListView,
    RecentProductsListView
)


class ProductUrlsTest(TestCase):
    """Tests for Products URLs."""

    def test_search_url(self):
        """"Resolves 'search' URL and view."""
        url = reverse('products:search')
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func, product_search)

    def test_prod_list_url(self):
        """"Resolves 'prod_list' URL and view."""
        url = reverse('products:prod_list')
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, ProductListView)

    def test_detail_url(self):
        """"Resolves 'detail' URL and view."""
        url = reverse('products:detail', args=[1])
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, ProductDetailView)

    def test_categories_url(self):
        """"Resolves 'categories' URL and view."""
        url = reverse('products:categories')
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, CategoriesListView)

    def test_category_filter_url(self):
        """"Resolves 'category_filter' URL and view."""
        url = reverse('products:category_filter', args=['slug_example'])
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, CategoryFilterListView)

    def test_deal_list_url(self):
        """"Resolves 'deal_list' URL and view."""
        url = reverse('products:deal_list')
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, DealListView)

    def test_deal_detail_url(self):
        """"Resolves 'deal_detail' URL and view."""
        url = reverse('products:deal_detail', args=['slug_example'])
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, DealDetailView)

    def test_brand_filter_url(self):
        """"Resolves 'brand_filter' URL and view."""
        url = reverse('products:brand_filter', args=['slug_example'])
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, BrandFilterListView)

    def test_recent_url(self):
        """"Resolves 'recent' URL and view."""
        url = reverse('products:recent')
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, RecentProductsListView)

"""URLs Tests for Product App."""

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
    RecentProductsListView,
)


class ProductsUrlsTest(TestCase):
    """Tests for Products URLs."""

    def test_search_url(self):
        url = reverse("products:search")
        resolver = resolve(url)
        self.assertEqual(resolver.func, product_search)

    def test_prod_list_url(self):
        url = reverse("products:prod_list")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ProductListView)

    def test_detail_url(self):
        url = reverse("products:detail", args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ProductDetailView)

    def test_categories_url(self):
        url = reverse("products:categories")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, CategoriesListView)

    def test_category_filter_url(self):
        url = reverse("products:category_filter", args=["slug_example"])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, CategoryFilterListView)

    def test_deal_list_url(self):
        url = reverse("products:deal_list")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, DealListView)

    def test_deal_detail_url(self):
        url = reverse("products:deal_detail", args=["slug_example"])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, DealDetailView)

    def test_brand_filter_url(self):
        url = reverse("products:brand_filter", args=["slug_example"])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, BrandFilterListView)

    def test_recent_url(self):
        url = reverse("products:recent")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, RecentProductsListView)

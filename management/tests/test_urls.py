"""URLs Tests for Management App."""

from django.test import TestCase
from django.urls import reverse, resolve

from management.views import (
    ManagementView,
    PageListView,
    PageUpdateView,
    ProductListView,
    DeactivatedProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductStatusToggleView,
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    BrandListView,
    BrandCreateView,
    BrandUpdateView,
    BrandDeleteView,
    DealListView,
    DealCreateView,
    DealUpdateView,
    DealDeleteView,
    UserListView,
)


class ManagementUrlsTest(TestCase):
    """Tests for Management URLs."""

    def test_management_url(self):
        url = reverse("management:management")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ManagementView)

    def test_page_list_url(self):
        url = reverse("management:page_list")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, PageListView)

    def test_page_update_url(self):
        url = reverse("management:page_update", args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, PageUpdateView)

    def test_product_list_url(self):
        url = reverse("management:product_list")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ProductListView)

    def test_product_deactivated_list_url(self):
        url = reverse("management:product_deactivated_list")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, DeactivatedProductListView)

    def test_product_create_url(self):
        url = reverse("management:product_create")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ProductCreateView)

    def test_product_update_url(self):
        url = reverse("management:product_update", args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ProductUpdateView)

    def test_product_delete_url(self):
        url = reverse("management:product_delete", args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ProductDeleteView)

    def test_product_deactivate_url(self):
        url = reverse("management:product_deactivate", args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ProductStatusToggleView)

    def test_product_activate_url(self):
        url = reverse("management:product_activate", args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ProductStatusToggleView)

    def test_category_list_url(self):
        url = reverse("management:category_list")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, CategoryListView)

    def test_category_create_url(self):
        url = reverse("management:category_create")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, CategoryCreateView)

    def test_category_update_url(self):
        url = reverse("management:category_update", args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, CategoryUpdateView)

    def test_category_delete_url(self):
        url = reverse("management:category_delete", args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, CategoryDeleteView)

    def test_brand_list_url(self):
        url = reverse("management:brand_list")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, BrandListView)

    def test_brand_create_url(self):
        url = reverse("management:brand_create")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, BrandCreateView)

    def test_brand_update_url(self):
        url = reverse("management:brand_update", args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, BrandUpdateView)

    def test_brand_delete_url(self):
        url = reverse("management:brand_delete", args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, BrandDeleteView)

    def test_deal_list_url(self):
        url = reverse("management:deal_list")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, DealListView)

    def test_deal_create_url(self):
        url = reverse("management:deal_create")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, DealCreateView)

    def test_deal_update_url(self):
        url = reverse("management:deal_update", args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, DealUpdateView)

    def test_deal_delete_url(self):
        url = reverse("management:deal_delete", args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, DealDeleteView)

    def test_user_list_url(self):
        url = reverse("management:user_list")
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, UserListView)

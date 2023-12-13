"""URLs Tests for the Management App."""

from django.test import TestCase
from django.urls import reverse, resolve
from management.views import (
    ManagementView,
    PageListView,
    PageUpdateView,
    UserListView,
    ProductListView,
    DeactivatedProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductStatusToggleView
)


class ManagementUrlsTest(TestCase):
    """Tests for Management URLs."""

    def test_management_url(self):
        """"Resolves 'management' URL and view."""
        url = reverse('management:management')
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, ManagementView)

    def test_page_list_url(self):
        """"Resolves 'page_list' URL and view."""
        url = reverse('management:page_list')
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, PageListView)

    def test_page_update_url(self):
        """"Resolves 'page_update' URL and view."""
        url = reverse('management:page_update', args=[1])
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, PageUpdateView)

    def test_user_list_url(self):
        """"Resolves 'user_list' URL and view."""
        url = reverse('management:user_list')
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, UserListView)

    def test_product_list_url(self):
        """"Resolves 'product_list' URL and view."""
        url = reverse('management:product_list')
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, ProductListView)

    def test_product_deactivated_list_url(self):
        """"Resolves 'product_deactivated_list' URL and view."""
        url = reverse('management:product_deactivated_list')
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, DeactivatedProductListView)

    def test_product_create_url(self):
        """"Resolves 'product_create' URL and view."""
        url = reverse('management:product_create')
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, ProductCreateView)

    def test_product_update_url(self):
        """"Resolves 'product_update' URL and view."""
        url = reverse('management:product_update', args=[1])
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, ProductUpdateView)

    def test_product_delete_url(self):
        """"Resolves 'product_delete' URL and view."""
        url = reverse('management:product_delete', args=[1])
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, ProductDeleteView)

    def test_product_deactivate_url(self):
        """"Resolves 'product_deactivate' URL and view."""
        url = reverse('management:product_deactivate', args=[1])
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, ProductStatusToggleView)

    def test_product_activate_url(self):
        """"Resolves 'product_activate' URL and view."""
        url = reverse('management:product_activate', args=[1])
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, ProductStatusToggleView)

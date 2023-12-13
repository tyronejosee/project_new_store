"""URLs Tests for the Home App."""

from django.test import TestCase
from django.urls import reverse, resolve
from home.views import IndexTemplateView, PageDetailView


class HomeUrlsTest(TestCase):
    """Tests for Home URLs."""

    def test_index_url(self):
        """"Resolves 'search' URL and view."""
        url = reverse('home:index')
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, IndexTemplateView)

    def test_page_detail_url(self):
        """"Resolves 'page_detail' URL and view."""
        url = reverse('home:page_detail', args=['key_example'])
        resolver = resolve(url)
        # Expected responses
        self.assertEqual(resolver.func.view_class, PageDetailView)

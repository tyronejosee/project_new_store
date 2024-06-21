"""Views Tests for Home App."""

from django.urls import reverse

from utils.tests import BaseTestCase


class HomeViewsTest(BaseTestCase):
    """Tests for Home views."""

    def test_index_view(self):
        """Test for IndexTemplateView."""
        url = reverse("home:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
        self.assertContains(response, self.product.title)

    def test_page_detail_view(self):
        """Test for PageDetailView."""
        url = reverse("home:page_detail", kwargs={"key": self.page.key})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/page_detail.html")
        self.assertEqual(response.context_data["page"], self.page)
        self.assertContains(response, self.page.content)

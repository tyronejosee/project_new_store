"""Views Tests for Management App."""

from django.urls import reverse

from utils.tests import BaseTestCase


class ManagementViewsTest(BaseTestCase):
    """Tests for Management views."""

    # Management tests
    def test_management_view(self):
        """Test for ManagementView."""
        url = reverse("management:management")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/dashboard.html")

    # Page tests
    def test_page_list_view(self):
        """Test for PageListView."""
        url = reverse("management:page_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/page_list.html")

    def test_page_update_view(self):
        """Test for PageUpdateView."""
        url = reverse("management:page_update", kwargs={"pk": self.page.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/page_form.html")

    # Product tests
    def test_product_list_view(self):
        """Test for ProductListView."""
        url = reverse("management:product_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/product_list.html")

    def test_product_create_view(self):
        """Test for ProductCreateView."""
        url = reverse("management:product_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/product_form.html")

    def test_product_update_view(self):
        """Test for ProductUpdateView."""
        url = reverse(
            "management:product_update",
            kwargs={"pk": self.product.pk},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/product_form.html")

    def test_product_delete_view(self):
        """Test for ProductDeleteView."""
        url = reverse(
            "management:product_delete",
            kwargs={"pk": self.product.pk},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_deactivated_product_list_view(self):
        """Test for DeactivatedProductListView."""
        url = reverse("management:product_deactivated_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/product_list.html")

    def test_product_status_toggle_view_deactivate(self):
        """Test for ProductStatusToggleView."""
        url = reverse("management:product_deactivate", args=[self.product.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_status_toggle_view_activate(self):
        """Test for ProductStatusToggleView."""
        url = reverse("management:product_activate", args=[self.product.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Category tests
    def test_category_list_view(self):
        """Test for CategoryListView."""
        url = reverse("management:category_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/category_list.html")

    def test_category_create_view(self):
        """Test for CategoryCreateView."""
        url = reverse("management:category_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/category_form.html")

    def test_category_update_view(self):
        """Test for CategoryUpdateView."""
        url = reverse(
            "management:category_update",
            kwargs={"pk": self.category.pk},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/category_form.html")

    def test_category_delete_view(self):
        """Test for CategoryDeleteView."""
        url = reverse(
            "management:category_delete",
            kwargs={"pk": self.category.pk},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "components/confirm_delete.html")

    # Brand tests
    def test_brand_list_view(self):
        """Test for BrandListView."""
        url = reverse("management:brand_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/brand_list.html")

    def test_brand_create_view(self):
        """Test for BrandCreateView."""
        url = reverse("management:brand_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/brand_form.html")

    def test_brand_update_view(self):
        """Test for BrandUpdateView."""
        url = reverse("management:brand_update", kwargs={"pk": self.brand.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/brand_form.html")

    def test_brand_delete_view(self):
        """Test for BrandDeleteView."""
        url = reverse("management:brand_delete", kwargs={"pk": self.brand.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "components/confirm_delete.html")

    # Deal tests
    def test_deal_list_view(self):
        """Test for DealListView."""
        url = reverse("management:deal_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/deal_list.html")

    def test_deal_create_view(self):
        """Test for DealCreateView."""
        url = reverse("management:deal_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/deal_form.html")

    def test_deal_update_view(self):
        """Test for DealUpdateView."""
        url = reverse("management:deal_update", kwargs={"pk": self.deal.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/deal_form.html")

    # User tests
    def test_user_list_view(self):
        """Test for UserListView."""
        url = reverse("management:user_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "management/user_list.html")

"""Models Tests for Home App."""

from django.test import TestCase

from home.models import Company, Page


class CompanyModelTest(TestCase):
    """Tests for Company model."""

    def setUp(self):
        self.company_data = {
            "name": "Example Company",
            "logo": "company/logo.png",
            "copy": "Example Copy",
            "description": "Example Description",
            "email": "example@example.com",
            "github": "https://github.com/example",
            "linkedin": "https://linkedin.com/example",
        }

    def test_create_company_instance(self):
        """Test creating a Company instance."""
        company = Company.objects.create(**self.company_data)
        self.assertEqual(company.name, "Example Company")
        self.assertEqual(company.description, "Example Description")
        self.assertNotEqual(company.name, "Example Error")

    def test_company_str_representation(self):
        """Test the string representation of a Company instance."""
        company = Company.objects.create(name="Example Company")
        self.assertEqual(str(company), "Example Company")

    def test_update_company_instance(self):
        """Test updating a Company instance."""
        company = Company.objects.create(name="Old Company Name")
        company.name = "New Company Name"
        company.save()
        self.assertEqual(company.name, "New Company Name")
        self.assertNotEqual(company.name, "Old Company Name")


class PageModelTest(TestCase):
    """Tests for Page model."""

    def setUp(self):
        self.page_data = {
            "key": "example_page",
            "content": "Example Content",
            "image": None,
        }

    def test_create_page_instance(self):
        """Test creating a Page instance."""
        page = Page.objects.create(**self.page_data)
        self.assertEqual(page.key, "example_page")

    def test_page_str_representation(self):
        """Test the string representation of a Page instance."""
        page = Page.objects.create(key="example_page")
        self.assertEqual(str(page), "example_page")

    def test_update_page_instance(self):
        """Test updating a Page instance."""
        page = Page.objects.create(key="Old Key")
        page.key = "New Key"
        page.save()
        self.assertEqual(page.key, "New Key")
        self.assertNotEqual(page.key, "Old Key")

"""Forms Tests for Management App."""

from django.test import TestCase

from products.models import Category, Brand, Deal
from management.forms import (
    PageForm,
    ProductForm,
    CategoryForm,
    BrandForm,
    DealForm,
)


class PageFormTest(TestCase):
    """Tests for PageForm."""

    # def test_valid_form(self):
    #     """Test if the form is valid with valid data."""
    #     data = {
    #         "key": "example_key",
    #         "content": "Example Content"
    #     }
    #     form = PageForm(data)
    #     self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if the form is invalid with empty data."""
        data = {}
        form = PageForm(data)
        self.assertFalse(form.is_valid())

    def test_key_length_limit(self):
        """Test if the form is invalid when "key" length exceeds the limit."""
        data = {
            "key": "example_key" * 10,  # max_length=50
            "content": "Lorem ipsum dolor sit amor.",
        }
        form = PageForm(data)
        self.assertFalse(form.is_valid())


class ProductFormTest(TestCase):
    """Tests for ProductForm."""

    def setUp(self):
        self.category = Category.objects.create(title="Test Category")
        self.brand = Brand.objects.create(name="Test Brand")
        self.deal = Deal.objects.create(name="Test Deal")

    # def test_valid_form(self):
    #     """Test if the form is valid with valid data."""
    #     data = {
    #         "title": "Example Product",
    #         "brand": self.brand.id,
    #         "normal_price": 100.00,
    #         "sale_price": 80.00,
    #         "deal": self.deal.id,
    #         "category": self.category.id,
    #         "image": None,
    #         "stock": 50,
    #         "warranty": 12,
    #         "featured": False,
    #         "show_hide": True,
    #         "description": "Example Description",
    #         "specifications": "Example Specifications",
    #     }
    #     form = ProductForm(data)
    #     self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if the form is invalid with empty data."""
        data = {}
        form = ProductForm(data)
        self.assertFalse(form.is_valid())

    def test_title_length_limit(self):
        """Test if the form is invalid when title length exceeds the limit."""
        data = {
            "title": "Invalid Title" * 10,  # max_length=255
        }
        form = ProductForm(data)
        self.assertFalse(form.is_valid())


class CategoryFormTest(TestCase):
    """Tests for CategoryForm."""

    def test_valid_form(self):
        """Test if the form is valid with valid data."""
        data = {
            "title": "Example Category",
            "slug": "example-category",
            "show_hide": True,
        }
        form = CategoryForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if the form is invalid with empty data."""
        data = {}
        form = CategoryForm(data)
        self.assertFalse(form.is_valid())

    def test_title_length_limit(self):
        """Test if the form is invalid when title length exceeds the limit."""
        data = {
            "title": "Example Title" * 10,  # max_length=50
            "slug": "example-category",
            "show_hide": True,
        }
        form = CategoryForm(data)
        self.assertFalse(form.is_valid())


class BrandFormTest(TestCase):
    """Tests for BrandForm."""

    def test_valid_form(self):
        """Test if the form is valid with valid data."""
        data = {
            "name": "Example Brand",
            "slug": "example-brand",
            "show_hide": True,
        }
        form = BrandForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if the form is invalid with empty data."""
        data = {}
        form = BrandForm(data)
        self.assertFalse(form.is_valid())

    def test_name_length_limit(self):
        """Test if the form is invalid when name length exceeds the limit."""
        data = {
            "name": "E" * 256,  # max_length=255
            "slug": "example-brand",
            "show_hide": True,
        }
        form = BrandForm(data)
        self.assertFalse(form.is_valid())


class DealFormTest(TestCase):
    """Tests for DealForm."""

    # def test_valid_form(self):
    #     """Test if the form is valid with valid data."""
    #     data = {
    #         "name": "Example Deal",
    #         "slug": "example-deal",
    #         "image": None,
    #         "description": "Example Description",
    #         "discount": 10,
    #         "start_date": "2023-01-01",
    #         "end_date": "2023-03-01",
    #         "status": True,
    #     }
    #     form = DealForm(data)
    #     self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if the form is invalid with empty data."""
        data = {}
        form = DealForm(data)
        self.assertFalse(form.is_valid())

    def test_name_length_limit(self):
        """Test if the form is invalid when name length exceeds the limit."""
        data = {
            "name": "E" * 256,  # max_length=255
            "slug": "example-deal",
            "image": "example_image.jpg",
            "description": "Example Description",
            "discount": 10,
            "start_date": "2023-01-01",
            "end_date": "2023-03-01",
            "status": True,
        }
        form = DealForm(data)
        self.assertFalse(form.is_valid())

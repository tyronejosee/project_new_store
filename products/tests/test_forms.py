"""Forms Tests for Product App."""

from django.test import TestCase

from products.models import Brand, Category, Deal
from products.forms import CategoriesForm


class ProductFormTest(TestCase):
    """Tests for category filter form."""

    def setUp(self):
        self.category = Category.objects.create(title="Example Category")
        self.brand = Brand.objects.create(name="Example Brand")
        self.deal = Deal.objects.create(name="Example Deal")

    def test_valid_form(self):
        """Test if the form is valid with valid data."""
        data = {
            "category": self.category.id,
            "brand": self.brand.id,
            "deal": self.deal.id,
            "min_price": 1,
            "max_price": 100,
        }
        form = CategoriesForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if the form is invalid with empty data."""
        data = {}
        form = CategoriesForm(data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        """Test form with invalid data."""
        data = {
            "category": "invalid_category",
            "brand": "invalid_brand",
            "deal": "invalid_deal",
            "min_price": "invalid_min_price",
            "max_price": "invalid_max_price",
        }
        form = CategoriesForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("category", form.errors)
        self.assertIn("brand", form.errors)
        self.assertIn("deal", form.errors)
        self.assertIn("min_price", form.errors)
        self.assertIn("max_price", form.errors)

"""Forms Tests for the Product App."""

from django.test import TestCase
from products.forms import CategoriesForm

class ProductFormTest(TestCase):
    """Tests for the category filter form in the Product App."""

    def test_form_blank_data(self):
        """Test form with blank data."""
        form = CategoriesForm(data={})
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        """Test form with invalid data."""
        form_data = {
            'category': 'invalid_category',
            'brand': 'invalid_brand',
            'deal': 'invalid_deal',
            'min_price': 'invalid_min_price',
            'max_price': 'invalid_max_price',
        }

        form = CategoriesForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors)
        self.assertIn('brand', form.errors)
        self.assertIn('deal', form.errors)
        self.assertIn('min_price', form.errors)
        self.assertIn('max_price', form.errors)

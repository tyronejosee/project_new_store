"""Models Tests for Product App."""

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from products.models import Category, Brand, Deal, Product


class CategoryModelTestCase(TestCase):
    """Tests for Category model."""

    def setUp(self):
        self.category = Category.objects.create(title="C Category Example")

    def test_title_max_length(self):
        """Test that the "title" field does not exceed the maximum length."""
        self.category.title = "A" * 51
        with self.assertRaises(ValidationError):
            self.category.full_clean()

    def test_slug_creation_on_save(self):
        """Test that slug is created correctly when saving a Category."""
        self.category.save()
        self.assertEqual(self.category.slug, slugify(self.category.title))

    def test_show_hide_default_value(self):
        """Test that the "show_hide" field has the default value."""
        self.assertTrue(self.category.show_hide)

    def test_ordering(self):
        """Test that the model is ordered by the "title" field."""
        Category.objects.create(title="B Category Example")
        Category.objects.create(title="A Category Example")
        categories = Category.objects.all()
        self.assertEqual(categories[0].title, "A Category Example")
        self.assertEqual(categories[1].title, "B Category Example")
        self.assertEqual(categories[2].title, "C Category Example")

    def test_str_representation(self):
        """Test that the string representation of the object is the title."""
        self.assertEqual(str(self.category), self.category.title)


class BrandModelTestCase(TestCase):
    """Tests for Brand model."""

    def setUp(self):
        self.brand = Brand.objects.create(name="Samsung")

    def test_name_max_length(self):
        """Test that the "name" field does not exceed the maximum length."""
        self.brand.name = "A" * 256
        with self.assertRaises(ValidationError):
            self.brand.full_clean()

    def test_slug_creation_on_save(self):
        """Test that slug is created correctly when saving a Brand."""
        self.brand.save()
        self.assertEqual(self.brand.slug, slugify(self.brand.name))

    def test_show_hide_default_value(self):
        """Test that the "show_hide" field has the default value."""
        self.assertTrue(self.brand.show_hide)

    def test_verbose_name_plural(self):
        """Test that plural name has been defined correctly in Meta class."""
        self.assertEqual(str(Brand._meta.verbose_name_plural), "brands")

    def test_ordering(self):
        """Test that the model is ordered by the "name" field."""
        Brand.objects.create(name="Apple")
        Brand.objects.create(name="Sony")
        brands = Brand.objects.all()
        self.assertEqual(brands[0].name, "Apple")
        self.assertEqual(brands[1].name, "Samsung")
        self.assertEqual(brands[2].name, "Sony")

    def test_str_representation(self):
        """Test that the string representation of the object is the name."""
        self.assertEqual(str(self.brand), self.brand.name)


class DealModelTestCase(TestCase):
    """Tests for Deal model."""

    def setUp(self):
        self.deal = Deal.objects.create(
            name="Special Deal",
            discount=15,
            start_date="2023-01-01",
            end_date="2023-01-31",
            status=True,
        )

    def test_name_max_length(self):
        """Test that the "name" field does not exceed the maximum length."""
        self.deal.name = "A" * 256
        with self.assertRaises(ValidationError):
            self.deal.full_clean()

    def test_slug_creation_on_save(self):
        """Test that slug is created correctly when saving a Deal."""
        self.deal.save()
        self.assertEqual(self.deal.slug, slugify(self.deal.name))

    def test_status_default_value(self):
        """Test that the "status" field has the default value."""
        self.assertTrue(self.deal.status)

    # TODO: ADD RENAME FILE TEST


class ProductModelTestCase(TestCase):
    """Tests for Product model."""

    def setUp(self):
        self.brand = Brand.objects.create(name="Samsung")
        self.category = Category.objects.create(title="Electronics")
        self.deal = Deal.objects.create(
            name="Special Deal",
            discount=15,
            start_date="2023-01-01",
            end_date="2023-01-31",
            status=True,
        )

    # def test_title_max_length(self):
    #     """Test that the "title" field does not exceed the maximum length."""
    #     product = Product.objects.create(
    #         title="A" * 256,
    #         brand=self.brand,
    #         normal_price=100,
    #         category=self.category
    #     )
    #     with self.assertRaises(ValidationError):
    #         product.full_clean()

    def test_slug_creation_on_save(self):
        """Test that slug is created correctly when saving a Product."""
        product = Product.objects.create(
            title="Test Product",
            brand=self.brand,
            normal_price=100,
            category=self.category,
        )
        product.save()
        self.assertEqual(product.slug, "test-product")

    def test_sale_price_calculation_without_deal(self):
        """Test that "update_sale_price" sets "sale_price" to None."""
        product = Product.objects.create(
            title="Test Product",
            brand=self.brand,
            normal_price=100,
            category=self.category,
        )
        product.update_sale_price()
        self.assertIsNone(product.sale_price)

    def test_is_new_method(self):
        """Test that the "is_new" method returns True."""
        product = Product.objects.create(
            title="Test Product",
            brand=self.brand,
            normal_price=100,
            category=self.category,
        )
        self.assertTrue(product.is_new())

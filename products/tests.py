"""Tests for the Products App."""

# FIX Product Detail and Product List
"""
from django.test import TestCase
from .models import Product, Brand, Category
from django.urls import reverse

class ProductModelTestCase(TestCase):
    """Unit tests for the Product model."""

    def setUp(self):
        # Create test objects for Brand and Category to use in tests
        self.brand = Brand.objects.create(name="Test Brand")
        self.category = Category.objects.create(title="Test Category")

        # Create a test Product object
        self.product = Product.objects.create(
            title="Test Product",
            brand=self.brand,
            normal_price=100.00,
            category=self.category,
            image="products/test.jpg",
            stock=50,
            warranty=12,
            discount_percentage=10.00,
            discount_end_date="2023-12-31",
            featured=True,
            show_hide=True,
            description="Test Description",
            specifications="Test Specifications"
        )

    def test_get_product(self):
        """Test retrieving a product."""
        response = self.client.get(reverse("product-detail", args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Product")

    def test_post_product(self):
        """Test creating a new product."""
        new_product_data = {
            "title": "New Product",
            "brand": self.brand.id,
            "normal_price": 150.00,
            "category": self.category.id,
            "image": "products/new.jpg",
            "stock": 75,
            "warranty": 24,
            "discount_percentage": 15.00,
            "discount_end_date": "2024-12-31",
            "featured": False,
            "show_hide": True,
            "description": "New Description",
            "specifications": "New Specifications"
        }

        response = self.client.post(reverse("product-list"), data=new_product_data, format="json")
        self.assertEqual(response.status_code, 201)

        # Verify that the new product has been created
        self.assertEqual(Product.objects.count(), 2)

    def test_put_product(self):
        """Test updating an existing product."""
        
        updated_product_data = {
            "title": "Updated Product",
            "normal_price": 120.00,
            "stock": 60,
            "description": "Updated Description"
        }

        response = self.client.put(reverse(
            "product-detail",
            args=[self.product.id]),
            data=updated_product_data,
            format="json")
        self.assertEqual(response.status_code, 200)

        # Refresh the object from the database
        self.product.refresh_from_db()
        self.assertEqual(self.product.title, "Updated Product")
        self.assertEqual(self.product.normal_price, 120.00)
        self.assertEqual(self.product.stock, 60)
        self.assertEqual(self.product.description, "Updated Description")

    def test_delete_product(self):
        """Test deleting an existing product."""
        response = self.client.delete(reverse("product-detail", args=[self.product.id]))
        self.assertEqual(response.status_code, 204)

        # Verify that the product has been deleted
        self.assertEqual(Product.objects.count(), 0)
"""

"""Tests for Home App."""

from django.test import TestCase
from .models import Page


class PageModelTestCase(TestCase):
    """Unit tests for the Page model"""

    def test_create_page(self):
        """Test the creation of a Page object in the database"""

        # Create an initial Page object with test key and content
        page = Page.objects.create(
            key="Test Key",
            content="Test content",
        )

        # Verify that there is an object in the database
        self.assertEqual(Page.objects.count(), 1)

        # Verify the key of the object
        self.assertEqual(page.key, "Test Key")

        # Verify the content of the object
        self.assertEqual(page.content, "Test content")

    def test_retrieve_page(self):
        """Test the retrieval of a Page object from the database"""

        # Create an initial Page object with test key and content
        page = Page.objects.create(
            key="Test Key",
            content="Test content",
        )

        # Retrieve the object by primary key
        retrieved_page = Page.objects.get(pk=page.pk)

        # Verify that the retrieved object is the same as the created one
        self.assertEqual(retrieved_page, page)

    def test_update_page(self):
        """Test the update of a Page object in the database"""

        # Create an initial Page object with test key and content
        page = Page.objects.create(
            key="Test Key",
            content="Test content",
        )

        # Change the key
        page.key = "New Key"

        # Save the updated object
        page.save()

        # Retrieve the updated object
        updated_page = Page.objects.get(pk=page.pk)

        # Verify the updated key
        self.assertEqual(updated_page.key, "New Key")

    def test_delete_page(self):
        """Test the deletion of a Page object from the database"""

        # Create an initial Page object with test key and content
        page = Page.objects.create(
            key="Test key",
            content="Test content",
        )

        # Delete the object
        page.delete()

        # Verify that there are no objects in the database
        self.assertEqual(Page.objects.count(), 0)

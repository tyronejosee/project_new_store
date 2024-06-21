"""Models Tests for Users App."""

from django.test import TestCase

from users.models import CustomUser


class CustomUserTests(TestCase):
    """Tests for creating a regular user and a superuser."""

    def test_create_user(self):
        """Test the creation of a regular user."""
        user = CustomUser
        user = user.objects.create_user(
            username="user_test",
            email="test@gmail.com",
            first_name="User",
            last_name="Test",
            password="testuser1234",
        )
        self.assertEqual(user.username, "user_test")
        self.assertEqual(user.email, "test@gmail.com")
        self.assertEqual(user.first_name, "User")
        self.assertEqual(user.last_name, "Test")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Test the creation of a superuser."""
        user = CustomUser
        user = user.objects.create_superuser(
            username="user_test",
            email="test@gmail.com",
            first_name="User",
            last_name="Test",
            password="testuser1234",
        )
        self.assertEqual(user.username, "user_test")
        self.assertEqual(user.email, "test@gmail.com")
        self.assertEqual(user.first_name, "User")
        self.assertEqual(user.last_name, "Test")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

"""Models Tests for the Users App."""

from django.test import TestCase
from users.models import CustomUser


class CustomUserTests(TestCase):
    """Tests for creating a regular user and a superuser."""

    def test_create_user(self):
        """Method testing the creation of a regular user."""

        user = CustomUser
        user = user.objects.create_user(
            username="usertest",
            email="test@gmail.com",
            first_name="User",
            last_name="Test",
            password="testuser1234"
        )
        # Expected results
        self.assertEqual(user.username, "usertest")
        self.assertEqual(user.email, "test@gmail.com")
        self.assertEqual(user.first_name, "User")
        self.assertEqual(user.last_name, "Test")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Method testing the creation of a superuser."""

        user = CustomUser
        user = user.objects.create_superuser(
            username="usertest",
            email="test@gmail.com",
            first_name="User",
            last_name="Test",
            password="testuser1234"
        )
        # Expected results
        self.assertEqual(user.username, "usertest")
        self.assertEqual(user.email, "test@gmail.com")
        self.assertEqual(user.first_name, "User")
        self.assertEqual(user.last_name, "Test")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

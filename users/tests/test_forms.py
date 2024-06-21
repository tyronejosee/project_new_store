"""Forms Tests for Users App."""

from django.test import TestCase

from users.forms import UserLoginForm, UserRegistrationForm, form_text


class UserLoginFormTest(TestCase):
    """Test for UserLoginForm."""

    def test_invalid_form(self):
        """Test if the form is invalid with invalid data."""
        data = {}
        form = UserLoginForm(data)
        self.assertFalse(form.is_valid())

    def test_widget_attributes(self):
        """Test if the widget attributes are configured correctly."""
        form = UserLoginForm()
        self.assertEqual(
            form.fields["username"].widget.attrs,
            form_text("Username"),
        )
        self.assertEqual(
            form.fields["username"].widget.attrs["placeholder"], "Username"
        )
        self.assertEqual(
            form.fields["password"].widget.attrs,
            form_text("Password"),
        )
        self.assertEqual(
            form.fields["password"].widget.attrs["placeholder"], "Password"
        )

    def test_labels_and_placeholders(self):
        """Test if the labels and placeholders are configured correctly."""
        form = UserLoginForm()
        self.assertEqual(
            form.fields["username"].label,
            "Username",
        )
        self.assertEqual(
            form.fields["username"].widget.attrs["placeholder"], "Username"
        )
        self.assertEqual(
            form.fields["password"].label,
            "Password",
        )
        self.assertEqual(
            form.fields["password"].widget.attrs["placeholder"], "Password"
        )


class UserRegistrationFormTest(TestCase):
    """Tests for UserRegistrationForm."""

    def test_valid_form(self):
        """Test if the form is valid with valid data."""
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
            "address": "123 Main St",
            "phone_number": "123456789",
            "password1": "example_password",
            "password2": "example_password",
        }
        form = UserRegistrationForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if the form is invalid with empty data."""
        data = {}
        form = UserRegistrationForm(data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_password_mismatch(self):
        """Test if the form is invalid when passwords do not match."""
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
            "address": "123 Main St",
            "phone_number": "123456789",
            "password1": "example_password",
            "password2": "mismatched_password",
        }
        form = UserRegistrationForm(data)
        self.assertFalse(form.is_valid())
        self.assertIn("Passwords do not match.", form.errors["password2"])

    def test_save_method(self):
        """Test if the save method correctly creates a new user."""
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
            "address": "123 Main St",
            "phone_number": "123456789",
            "password1": "example_password",
            "password2": "example_password",
        }
        form = UserRegistrationForm(data)
        self.assertTrue(form.is_valid())

        # Save method
        user = form.save(commit=False)
        user.save()

        self.assertIsNotNone(user.pk)
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")
        self.assertEqual(user.address, "123 Main St")
        self.assertEqual(user.phone_number, "123456789")
        self.assertNotEqual(user.username, "userinvalid")

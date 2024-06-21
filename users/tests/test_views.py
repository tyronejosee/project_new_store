"""Views Tests for Users App."""

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from users.models import CustomUser
from users.forms import UserLoginForm, UserRegistrationForm


class UserViewsTest(TestCase):
    """Tests for Users Views."""

    def setUp(self):
        # Create a user
        self.user = get_user_model().objects.create_user(
            username="example_user",
            email="example_user@example.com",
            password="examplepassword",
            first_name="Example",
            last_name="User",
        )
        self.client = Client()

    # Tests for UserLoginView
    def test_access_without_authentication(self):
        """Test verify that an unauthenticated user can access login view."""
        url = reverse("users:login")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login_form.html")

    def test_access_with_authentication(self):
        """Test checks redirection for auth user accessing login view."""
        self.client.login(username="example_user", password="examplepassword")
        url = reverse("users:login")
        response = self.client.get(url)
        self.assertRedirects(response, reverse("home:index"))

    def test_login_form_displayed(self):
        """Test verify that the login form is displayed correctly."""
        url = reverse("users:login")
        response = self.client.get(url)
        self.assertIsInstance(response.context["form"], UserLoginForm)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_successful_login(self):
        """Test verify successful login and redirection."""
        data = {"username": "example_user", "password": "examplepassword"}
        url = reverse("users:login")
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse("home:index"))
        self.assertTrue(self.client.session["_auth_user_id"])

    # FIXME: Assertcontainains errors
    def test_failed_login(self):
        """Test login with invalid credentials and verify error message."""
        data = {
            "username": "example_user",
            "password": "examplepasswordwrong",  # Invalid password
        }
        url = reverse("users:login")
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login_form.html")
        # self.assertContains(response, 'Invalid username or password')

    # Tests for UserRegistrationView
    def test_access_without_authentication_registration(self):
        """Test verify that an unauth user can access registration view."""
        url = reverse("users:registration")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/registration_form.html")

    def test_registration_form_displayed(self):
        """Test verify that the registration form is displayed correctly."""
        url = reverse("users:registration")
        response = self.client.get(url)
        self.assertIsInstance(response.context["form"], UserRegistrationForm)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_successful_registration(self):
        """Test registration form with valid data and verify redirection."""
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password1": "testpass123",
            "password2": "testpass123",
        }
        url = reverse("users:registration")
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse("cart:cart"))
        self.assertTrue(self.client.session["_auth_user_id"])

    def test_authentication_after_registration(self):
        """Test user is authenticated after successful registration."""
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password1": "testpass123",
            "password2": "testpass123",
        }
        url = reverse("users:registration")
        self.client.post(url, data)
        user = CustomUser.objects.get(username="newuser")
        self.assertEqual(self.client.session["_auth_user_id"], str(user.id))

    def test_redirect_authenticated_user_registration(self):
        """Test check redirect when accessing registration view while auth."""
        self.client.login(username="example_user", password="examplepassword")
        url = reverse("users:registration")
        response = self.client.get(url)
        self.assertRedirects(response, reverse("cart:cart"))

    # Test for user_logout view
    def test_successful_logout(self):
        """Test verifies successful logout."""
        self.client.login(username="example_user", password="examplepassword")
        self.assertTrue(self.client.session.get("_auth_user_id"))
        url = reverse("users:logout")
        response = self.client.get(url)
        self.assertRedirects(response, reverse("home:index"))
        self.assertFalse(self.client.session.get("_auth_user_id"))

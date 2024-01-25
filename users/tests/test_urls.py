"""URLs Tests for Users App."""

from django.test import TestCase
from django.contrib.auth.views import PasswordResetDoneView
from django.urls import reverse, resolve
from users.views import (
    UserLoginView,
    user_logout,
    UserRegistrationView,
    PasswordChangeView
)


class UserUrlsTest(TestCase):
    """Tests for Users URLs."""

    def test_login_url(self):
        """"Test resolves 'login' URL and view."""
        url = reverse('users:login')
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, UserLoginView)

    def test_logout_url(self):
        """"Test resolves 'logout' URL and view."""
        url = reverse('users:logout')
        resolver = resolve(url)
        self.assertEqual(resolver.func, user_logout)

    def test_registration_url(self):
        """"Test resolves 'registration' URL and view."""
        url = reverse('users:registration')
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, UserRegistrationView)

    def test_password_change_url(self):
        """"Test resolves 'password_change' URL and view."""
        url = reverse('users:password_change')
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, PasswordChangeView)

    def test_password_change_done_url(self):
        """"Test resolves 'password_change_done' URL and view."""
        url = reverse('users:password_change_done')
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, PasswordResetDoneView)

"""Views for Products App."""

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django import forms
from users.models import Profile
from users.forms import UserCreationFormWithEmail, ProfileForm, EmailForm


class SignUpView(CreateView):
    """View for user registration (Sign Up)."""
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        """Get the URL to redirect to after a successful registration."""
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        """Customize the appearance of the registration form fields."""
        form = super(SignUpView, self).get_form()
        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Username'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Password'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Confirm the password'})
        return form


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    """View for updating user profile information."""
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        """Get the user's custom profile object for editing."""
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    """View for updating the user's email."""
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        """Retrieve the user whose email is being edited."""
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        # Modify in real-time
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        return form


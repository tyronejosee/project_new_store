

# models.py

from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from users.views import WelcomeView, SignUpView, ProfileUpdate, EmailUpdate
from django.utils.decorators import method_decorator
from users.forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from users.models import Profile
from django import forms
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


def custom_upload_to(instance, filename):
    """Custom file upload path for profile avatars."""
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename


class Profile(models.Model):
    """Model extending fields from the User class."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        """Meta definition for Profile."""
        ordering = ['user__username']


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    """Signal creates a User profile when a new User is saved."""
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)

# views.py


class WelcomeView(LoginRequiredMixin, TemplateView):
    """User welcome view."""
    template_name = 'users/welcome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context


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
            attrs={'class': 'form-control mb-2', 'placeholder': 'Username'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Password'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Confirm the password'})
        return form


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    """View for updating user profile information."""
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    def get_object(self):
        """Get the user's custom profile object for editing."""
        profile, created = Profile.objects.get_or_create(
            user=self.request.user)
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
            attrs={'class': 'form-control mb-2', 'placeholder': 'Email'})
        return form

# urls.py


urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
    path('welcome/', WelcomeView.as_view(), name="welcome"),
]


# forms.py


class UserCreationFormWithEmail(UserCreationForm):
    """Custom user creation form with an additional email field."""
    email = forms.EmailField(required=True, help_text="Requirement: 254")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        """Validate the uniqueness of the email address."""
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Email is already registered, please try another.")
        return email


class ProfileForm(forms.ModelForm):
    """Form for editing user profile information."""
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Biography'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Links'}),
        }


class EmailForm(forms.ModelForm):
    """Form for editing a user's email address."""
    email = forms.EmailField(
        required=True, help_text="Required. Maximum 254 characters")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        """Validate the email address for uniqueness."""
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "Email is already registered, please try another.")
        return email

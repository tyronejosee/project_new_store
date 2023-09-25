"""Forms for Products App."""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import CustomUser


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
            raise forms.ValidationError("Email is already registered, please try another.")
        return email


class CustomUserForm(forms.ModelForm):
    """Form for editing custom user profile information."""
    class Meta:
        model = CustomUser
        fields = ['address', 'city', 'country']
        widgets = {
            'address': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografía'}),
            'city': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografía'}),
            'country': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografía'}),
        }


class EmailForm(forms.ModelForm):
    """Form for editing a user's email address."""
    email = forms.EmailField(required=True, help_text="Required. Maximum 254 characters")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        """Validate the email address for uniqueness."""
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Email is already registered, please try another.")
        return email

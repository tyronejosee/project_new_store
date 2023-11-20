"""Forms for Users App."""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from core.utils import form_text_input
from users.models import CustomUser


class UserLoginForm(AuthenticationForm):
    """Base form for user login."""

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = form_text_input('Username')
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs = form_text_input('Password')
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class UserRegistrationForm(forms.ModelForm):
    """Base form for user registration."""

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs=form_text_input('Password')
    ))

    password2 = forms.CharField(label='Repeat your password', widget=forms.PasswordInput(
        attrs=form_text_input('Repeat your password')
    ))

    class Meta:
        """Meta definition for UserRegistrationForm."""
        model = CustomUser
        fields = ('username', 'email', 'first_name',
                  'last_name', 'address', 'phone_number')
        widgets = {
            'username': forms.TextInput(attrs=form_text_input('Username')),
            'email': forms.EmailInput(attrs=form_text_input('Email')),
            'first_name': forms.TextInput(attrs=form_text_input('First Name')),
            'last_name': forms.TextInput(attrs=form_text_input('Last Name')),
            'address': forms.TextInput(attrs=form_text_input('Address')),
            'phone_number': forms.TextInput(attrs=form_text_input('Phone Number')),
        }

    def clean_password2(self):
        """Validates and compares passwords."""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return password2

    def save(self, commit=True):
        """Save the user instance with password hashing."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

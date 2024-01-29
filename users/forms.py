"""Forms for Users App."""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from users.models import CustomUser
from utils.tailwind_classes import form_text, form_number


class UserLoginForm(AuthenticationForm):
    """Base form for user login."""

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = form_text('Username')
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs = form_text('Password')
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class UserRegistrationForm(forms.ModelForm):
    """Base form for user registration."""

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs=form_text('Password')
    ))

    password2 = forms.CharField(label='Repeat your password', widget=forms.PasswordInput(
        attrs=form_text('Repeat your password')
    ))

    class Meta:
        """Meta definition for UserRegistrationForm."""
        model = CustomUser
        fields = ('username', 'email', 'first_name',
                  'last_name', 'address', 'phone_number')
        widgets = {
            'username': forms.TextInput(attrs=form_text('Username')),
            'email': forms.EmailInput(attrs=form_text('Email')),
            'first_name': forms.TextInput(attrs=form_text('First Name')),
            'last_name': forms.TextInput(attrs=form_text('Last Name')),
            'address': forms.TextInput(attrs=form_text('Address')),
            'phone_number': forms.NumberInput(attrs=form_number('Phone Number')),
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


class ThemePreferenceForm(forms.Form):
    """Base form for Theme Preference."""
    THEME_CHOICES = [
        ('dark', 'Dark'),
        ('light', 'Light'),
    ]
    theme_preference = forms.ChoiceField(
        choices=THEME_CHOICES,
        widget=forms.Select(
            attrs={'class': 'btn btn--secondary block w-full', 'onchange': 'submit()'}
        ),
        label=False
    )

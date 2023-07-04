from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class PasswordResetRequestForm(forms.Form):
    email_or_username = forms.CharField(label=("Email Or Username"), max_length=254)

class SetPasswordForm(forms.Form):
    password = forms.CharField(label=("New Password"), widget=forms.PasswordInput)
    password_confirmation = forms.CharField(label=("Confirm New Password"), widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(SetPasswordForm, self).clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError("Password and Confirm password does not match.")
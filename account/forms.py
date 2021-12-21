from django.contrib.auth.forms import AuthenticationForm
from django import forms

from account.models import CustomUser


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, label='username')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label='password')
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput, label='confirm password')

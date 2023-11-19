from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'city', 'password1', 'password2', 'image')

class EditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'city', 'image')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

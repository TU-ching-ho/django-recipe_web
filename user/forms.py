from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Recipe

# 註冊表單


class Registerform(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# 創建食譜表單


class createRecipe(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'text', 'image']

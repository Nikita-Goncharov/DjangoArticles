import email
from unicodedata import name
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, ClearableFileInput, Select
from django.contrib.auth.forms import  AuthenticationForm
from .models import *

from django.core.mail import send_mail


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input username', 'placeholder': 'Username'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input email', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input password1', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input password2', 'placeholder': 'Repeat password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input username', 'placeholder': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input password', 'placeholder': 'Password'}))


class WriteArticleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Сategory not selected'

    class Meta:
        model = Article
        fields = ['title', 'content', 'photo', 'category']
        widgets = {
            'title': TextInput(attrs={'class': 'title', 'placeholder': 'Title'}),
            'content': Textarea(attrs={'class': 'content_form', 'placeholder': 'Content'}),
            'photo': ClearableFileInput(attrs={'class': 'form-control form-control-sm photo'}),
            'category': Select(attrs={'class': 'category'}),
        }


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control username', 'placeholder': 'Name'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control email', 'placeholder': 'Email'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control message', 'placeholder': 'Message'}))


from django import forms

from .models import Account
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordResetForm, SetPasswordForm)


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(
        max_length=20, min_length=5, label="Enter UserName")
    email = forms.EmailField(max_length=200, help_text="Required", error_messages={
                             'Required': 'Sorry,please enter a valid email address'})
    password1 = forms.CharField(
        max_length=15, min_length=8, label="Enter Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        max_length=15, min_length=8, label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'user_name')

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        n = Account.objects.filter(user_name=user_name)
        if n.count():
            raise forms.ValidationError("username already exist")
        return user_name

    def clean_password2(self):
        cp = self.cleaned_data
        if cp['password1'] != cp['password2']:
            raise forms.ValidationError('Passwords do not match!')
        return cp['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Account.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "email address already exist, please user another one!")
        return email

    # for us to be able to customize the frontend of the form add the classes
    # and other info to be used


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())

    password = forms.CharField(widget=forms.PasswordInput())


class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = Account.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Unfortunately we can not find that email address')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))


class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-firstname', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-lastname'}))

    class Meta:
        model = Account
        fields = ('email', 'user_name', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['email'].required = True

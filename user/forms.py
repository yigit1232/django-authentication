from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Name'}),
        required=False,
        max_length=255,
    )
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Username'}),
        required=False,
        max_length=255,
    )
    email = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email'}),
        required=False,
        max_length=255,
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Password'}),
        required=False,
        max_length=255,
    )
    repassword = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Password(again)'}),
        required=False,
        max_length=255,
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Username'}),
        required=False,
        max_length=255,
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Password'}),
        required=False,
        max_length=255,
    )

class ForgotPasswordForm(forms.Form):
    email = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email'}),
        required=False,
        max_length=255,
    )

class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Password'}),
        required=False,
        max_length=255,
    )
    repassword = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Password(again)'}),
        required=False,
        max_length=255,
    )
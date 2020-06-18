from allauth.account.forms import LoginForm as AllAuthLoginForm
from allauth.account.forms import SignupForm as AllAuthSignupForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(AllAuthSignupForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'last name',
            'required': '',
            'class': 'signup_field'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'first name',
            'required': '',
            'class': 'signup_field'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'email',
            'required': '',
            'class': 'signup_field'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'password',
            'required': '',
            'class': 'signup_field'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'password',
            'required': '',
            'class': 'signup_field'
        })


class LoginForm(AllAuthLoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'placeholder': 'Login',
            'required': '',
            'class': 'authorization_field'
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': 'Password',
            'required': '',
            'class': 'authorization_field'
        })


class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Имя',
            'required': '',
            'class': 'edit signup_field'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Фамилия',
            'required': '',
            'class': 'edit signup_field'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Почта',
            'required': '',
            'class': 'edit signup_field'
        })

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar']

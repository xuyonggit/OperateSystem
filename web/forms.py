#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="",
        error_messages={'required': 'Please input user name!'},
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'id': 'inputSuccess1'
            },
        ),
    )
    password = forms.CharField(
        required=True,
        label="",
        error_messages={'required': 'Please input user passwd!'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control',
                'id': 'inputSuccess1'
            },
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u'用户名为必填项')
        else:
            cleaned_data = super(LoginForm, self).clean()

class resetpasswd(forms.Form):
    username = forms.CharField(
        required=True,
        label="",
        error_messages={'required': 'Please input user name!'},
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                'id': 'inputSuccess1'
            },
        ),
    )
    resetquestion = forms.CharField(
        required=True,
        label="",
        error_messages={'required': 'Please input The answer'},
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Answer',
                'class': 'form-control',
                'id': 'inputSuccess1'
            },
        ),
    )

    newpasswd = forms.CharField(
        required=True,
        label="",
        error_messages={'required': 'Please input The answer'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'New Password',
                'class': 'form-control',
                'id': 'inputSuccess1'
            },
        ),
    )
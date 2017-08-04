#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="账户",
        error_messages={'required': 'Please input user name!'},
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
            },
        ),
    )
    password = forms.CharField(
        required=True,
        label="密码",
        error_messages={'required': 'Please input user passwd!'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
            },
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u'用户名为必填项')
        else:
            cleaned_data = super(LoginForm, self).clean()

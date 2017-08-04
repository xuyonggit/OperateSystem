#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput

#class LoginForm(forms.Form):
#	username = forms.CharField(
#		required=True,
#		label="用户名",
#		error_messages={'required': 'Please input user name!'},
#		widget=forms.TextInput(
#			attrs={
#				'placeholder': '用户名',
#			},
#		),
#	)
#	password = forms.CharField(
#		required=True,
#		label="密码",
#		error_messages={'required': 'Please input user passwd!'},
#		widget=forms.PasswordInput(
#			attrs={
#				'placeholder': '密码',
#			},
#		),
#	)
#	def clean(self):
#		if not self.is_valid():
#			raise forms.ValidationError(u'用户名为必填项')
#		else:
#			cleaned_data = super(LoginForm, self).clean()
#
class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密__码',widget=forms.PasswordInput())

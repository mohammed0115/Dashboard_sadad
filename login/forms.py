from django import forms
#from dappx.models import UserProfileInfo
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

class UserForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    phone = PhoneNumberField()






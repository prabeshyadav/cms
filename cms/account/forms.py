from django import forms
from cms import common
from .models import *

class CustomerRegister(forms.Form):
    username = forms.CharField()
    name = forms.CharField()
    email = forms.EmailField()
    address=forms.CharField()
    phone_number = forms.CharField(required=False)
    role = forms.ChoiceField(choices=common.USER_ROLES)

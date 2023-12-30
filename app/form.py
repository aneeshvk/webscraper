from django import forms
from .models import ureg


class UregCreate(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = ureg
        fields = ['firstname','lastname', 'email', 'password']
        labels = {'firstname': 'First Name','lastname':'Last Name', 'email': 'Email','password': 'Password'}

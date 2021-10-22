from user import forms
from django import forms 
from django.db.models import fields
from .models import Name


class Regform(forms.ModelForm):
    class Meta:
        model = Name
        fields = ('name','surname')
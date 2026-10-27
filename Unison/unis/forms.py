from django import forms
from .models import unis

class UnisForm(forms.ModelForm):
    class meta:
        model = unis
        fields = ['text' , 'photo']
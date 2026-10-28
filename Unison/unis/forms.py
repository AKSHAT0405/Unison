from django import forms
from .models import unis

class UnisForm(forms.ModelForm):
    class Meta:
        model = unis
        fields = ['text' , 'photo']
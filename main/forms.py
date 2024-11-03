
from django import forms
from .models import MainModel 

class MainModelForm(forms.ModelForm):
    class Meta:
        model = MainModel
        fields = '__all__'  

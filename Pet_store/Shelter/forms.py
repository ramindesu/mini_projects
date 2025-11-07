from .models import Owner
from django import forms

class OwnerForms(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name' , 'phone']

    

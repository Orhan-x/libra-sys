from django import forms
from .models import Registration


class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = Registration
        
        fields = [
            'cni',
            'f_name',
            'l_name',
            'phone_number',
            'email',
        ]


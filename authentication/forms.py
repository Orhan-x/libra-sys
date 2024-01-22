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
        
        labels = {
            'cni':'Carte National',
            'f_name':"First Name" ,
            'l_name': 'Last Name ',
            'phone_number': 'Phone Number',
            'email': 'E-mail',
        }


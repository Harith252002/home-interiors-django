
from django.contrib.auth.hashers import make_password
from django import forms
from .models import User   

class Registerform(forms.ModelForm):
    class Meta:
        model = User   
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password']

    # Add the widget to hide the password input
    username = forms.CharField(
        max_length=150,
        error_messages={
            'required': '', 
            'max_length': '',  
            'invalid': '',  
        }
    )
    password = forms.CharField(widget=forms.PasswordInput())   

    def save(self, commit=True):
        s = super().save(commit=False)
        s.password = make_password(self.cleaned_data['password'])  
        if commit:
            s.save()
        return s

# Login Form
class Loginform(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=128,widget=(forms.PasswordInput()))
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import PasswordInput
from .models import CustomUser

class UserForm(forms.Form):
    name=forms.CharField(label='Name',max_length=30,required=True, 
                     widget=forms.TextInput(attrs={'class': 'form-control'}))

    username=forms.CharField(label='Username',max_length=30, required=True,
                         widget=forms.TextInput(attrs={'class': 'form-control'}))

    email=forms.EmailField(label='Email',required=True,
                       widget=forms.EmailInput(attrs={'class': 'form-control'}))

    password=forms.CharField(label='Password',max_length=20, required=True,  
                         widget=PasswordInput(attrs={'class': 'form-control'}),validators=[validate_password])

    cpassword=forms.CharField(label='Confirm Password',max_length=20, required=True,
                          widget=PasswordInput(attrs={'class': 'form-control'}))
    
    image = forms.ImageField(label='Image', required=False,  
                         widget=forms.FileInput(attrs={
    'class': 'form-control-file'}))

    bio=forms.CharField(label='Bio',max_length=100,widget=forms.Textarea(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data=self.cleaned_data
        username = self.data.get('username')  
        password = self.data.get('password')
        cpassword = self.data.get('cpassword')
        if cpassword!=password:
            raise ValidationError("Passwords dont match!")
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Username already exsists!")
        return cleaned_data
            
        
    

class SignInForm(forms.Form):
    username=forms.CharField(label='Username',max_length=30, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label='Password',max_length=20, required=True,widget=PasswordInput(attrs={'class': 'form-control'}))
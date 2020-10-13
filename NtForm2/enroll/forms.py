from django import forms
from django.core import validators
from .models import User

class StudentRegistration(forms.ModelForm):

    # name=forms.CharField(widget=forms.TextInput(),error_messages={'required':'enter your name'})
    # email=forms.EmailField(error_messages={'required':'enter your email'})
    # password=forms.CharField(widget=forms.PasswordInput(), max_length=10,error_messages={'required':'enter your password'})

    class Meta:
        model=User
        fields={'name','email','password'}
        labels={'name':'Enter Name','email':'Enter Email','password':'Enter Password'}
        error_messages={
                'name':{'required':'Enter your Name'},
                'email':{'required':'Enter your Email'},
                'password':{'required':'Enter your Password'}}
        widgets={
            'name':forms.TextInput(attrs={'class':'myclass','placeholder':'yaha likho'}),
            'password':forms.PasswordInput,
            }




    
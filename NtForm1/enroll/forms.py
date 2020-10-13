from django import forms
from django.core import validators

def starts_with_s(value):
    if value[0]!='s':
        raise forms.ValidationError('Name should starts with s')


class StudentRegistration(forms.Form):
    error_css_class='error'
    required_css_class='required'
    
    name=forms.CharField( help_text= 'limit 10 characters',widget=forms.TextInput(attrs={'class':'nitesh'}),strip=False,empty_value='sonam',min_length=5)
    email=forms.EmailField(error_messages={'required':'Enter your email'})
    password=forms.CharField(widget=forms.PasswordInput())
    repassword=forms.CharField(widget=forms.PasswordInput(), label='Re-password')

    agree=forms.BooleanField(label='I Agree', required=False)
    roll=forms.IntegerField(min_value=5, required=False, label='Roll no')
    notes=forms.CharField(widget=forms.Textarea(attrs={'rows':3,'col':50}), max_length=50 )
    relation = forms.CharField(validators=[starts_with_s])

    # def clean_name(self):
    #     valname= self.cleaned_data['name'] 
    #     valemail= self.cleaned_data['email'] 

    #     if len(valname)<8:
    #         raise forms.ValidationError('Enter more than or equal to 8')
    #     return valname

    #     if len(valemail)<10:
    #         raise forms.ValidationError('Enter more than or equal to 10')
    #     return valemail


    # def clean(self):
    #     cleaned_data=super().clean()
    #     valpwd=cleaned_data['password']
    #     valrpwd=cleaned_data['repassword']
        
    #     if valpwd!= valrpwd:
    #         raise forms.ValidationError('Password Not Matched')
        
            
            
        

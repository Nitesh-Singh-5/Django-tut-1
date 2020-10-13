from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField(label="your name",initial='nitesh',help_text= 'limit 10 characters',widget=forms.PasswordInput(attrs={'class':'somecss'}))
    email=forms.EmailField()

    
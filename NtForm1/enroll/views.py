from django.shortcuts import render
from .forms import StudentRegistration 

from django.http import HttpResponseRedirect

# Create your views here.
def thankyou(request):
    return render(request,'enroll/success.html')

def ShowFormData(request):
    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            name= fm.cleaned_data['name']
            email= fm.cleaned_data['email']
            password= fm.cleaned_data['password']
            repassword= fm.cleaned_data['repassword']
            agree=fm.cleaned_data['agree']
            roll=fm.cleaned_data['roll']

            print('Name:',name)
            print('Email:',email)
            print('password:',password)
            print('agree:',agree)
            print('roll:',roll)
            print('re-password',repassword)

            fm=StudentRegistration()

            # return render(request,'enroll/success.html',{'nm':name})
            return HttpResponseRedirect('/ho/success')
            
    else:
        fm=StudentRegistration()
        print("ye get request se aya hai")
    return render(request,'enroll/home.html',{'form':fm})


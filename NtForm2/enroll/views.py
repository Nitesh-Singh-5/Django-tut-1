from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def showdata(request):
    if request.method== 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pas=fm.cleaned_data['password']
            
            # print('name:',name)
            # print('email:',email)
            # print('password:',password)

            reg = User(name=nm,email=em,password=pas)
            reg.save()

            # reg= User(id=3)
            # reg.delete()
            

    fm=StudentRegistration()
    return render(request,'enroll/home.html',{'form':fm})




from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.contrib import messages

# Create your views here.
def regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS,'Your Account has been Created')
            messages.info(request, 'WElcome')


    else:
        fm=StudentRegistration()
    return render(request, 'enroll/registration.html',{'form':fm})
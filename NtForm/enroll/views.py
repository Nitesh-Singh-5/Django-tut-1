from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def showformdata(request):
    fm = StudentRegistration(auto_id='name',label_suffix=" ")
    return render(request, 'enroll/core.html' , {'form':fm})
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn1(request):
    return render(request,"courseone.html")

def study1(request):
    return render(request,'coursetwo.html')
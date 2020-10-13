from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learn(request):
    return HttpResponse("<h1>hello Gorakhpur</h1>")

def study(request):
    return HttpResponse("hello dumri")
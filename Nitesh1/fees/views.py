from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn1(request):
    return HttpResponse("hello Gorakhpur")

def study1(request):
    return HttpResponse("hello dumri")
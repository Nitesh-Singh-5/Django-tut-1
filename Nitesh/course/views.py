from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return HttpResponse('<h1>Hello Nitesh</h1>')


def Services(request):
    return HttpResponse('<h1>Hello Services</h1>')


def format(request):
    a = 'Nitesh Singh'
    return HttpResponse(f'hello {a}')
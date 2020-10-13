from django.shortcuts import render

# Create your views here.

def learn(request):
    cn = {'cname': 'Javascript'}
    return render(request,'courseone.html',cn)

def study(request):
    return render(request,'coursetwo.html')
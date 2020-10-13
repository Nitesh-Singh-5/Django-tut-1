from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'core/home.html',{'cname':'Django',})


def learn(request):
    return render(request,'core/about.html',{'cname':'Python',})
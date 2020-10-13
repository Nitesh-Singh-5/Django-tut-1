from django.shortcuts import render

# Create your views here.

def study(request):
    return render(request, 'fees/info.html', {'nm':'Django Fees'})
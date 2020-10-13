from django.urls import path 
from . import views

urlpatterns = [
    path('home/',views.showdata, name='home')
]

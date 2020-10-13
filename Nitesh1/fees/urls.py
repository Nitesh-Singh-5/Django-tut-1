from django.urls import path
from . import views

urlpatterns = [
    path('study1/', views.study1),
    path('learn1/', views.learn1),
]

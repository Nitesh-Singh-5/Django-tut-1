from django.urls import path
from . import views

urlpatterns = [
    path('study/', views.study),
    path('learn/', views.learn),
]

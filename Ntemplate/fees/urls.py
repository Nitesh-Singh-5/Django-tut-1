from django.urls import path
from fees import views
urlpatterns = [
    path('learn1/',views.learn1),
    path('study1/',views.study1),
    ]

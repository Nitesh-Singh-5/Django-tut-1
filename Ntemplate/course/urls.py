from django.urls import path
from course import views
urlpatterns = [
    path('learn/',views.learn),
    path('study/',views.study),
    ]

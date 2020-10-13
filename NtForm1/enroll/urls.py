from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.ShowFormData, name='home'),
    path('success/',views.thankyou)
]

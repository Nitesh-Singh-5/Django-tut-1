from django.shortcuts import render
from enroll.models import Student
# Create your views here.

def studentinfo(request):
    stud = Student.objects.all()
    return render(request, 'enroll/studetails.html', {'stu': stud})

def __str__(self):
    return self.stuname
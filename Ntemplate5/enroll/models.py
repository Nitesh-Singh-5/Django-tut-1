from django.db import models


class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=70 ,default="")
    stuemail = models.EmailField(max_length=70 ,default="")
    stupass = models.CharField(max_length=70 ,default="")
    # stucom = models.CharField(max_length=70 ,default="")



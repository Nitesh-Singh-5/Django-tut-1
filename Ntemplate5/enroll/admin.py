from django.contrib import admin
from .models import Student
# Register your models here.


@admin.register(Student)                         # this is using in place of admin.site.register...

class StudentAdmin(admin.ModelAdmin):        # For making in rows
    list_display=('stuid','stuname','stuemail','stupass')


# admin.site.register(Student, StudentAdmin )

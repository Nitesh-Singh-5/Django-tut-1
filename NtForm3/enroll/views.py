from django.shortcuts import render

# Create your views here.
def detail(request):
    return render(request,'enroll/show.html')

# def showdata(request,my_id):
#     student={'id':my_id}
#     return render(request,'enroll/home.html',student)


def showdata(request,my_id):
    if my_id == '1':
        student = {'id':my_id, 'name':'rohan'}
    
    if my_id == '2':
        student = {'id':my_id, 'name':'Harsh'}

    if my_id == '3':
        student = {'id':my_id, 'name':'sonam'}
    return render(request,'enroll/home.html',student)
    


def showsubdata(request,my_id,my_subid):
    if my_id == 1 and my_subid == 5:
        student = {'id':my_id, 'name':'rohan','info':'sub details'}
    
    if my_id == 2 and my_subid == 6:
        student = {'id':my_id, 'name':'Harsh','info':'sub details'}

    if my_id == 3 and my_subid == 7:
        student = {'id':my_id, 'name':'sonam','info':'sub details'}
    
    return render(request,'enroll/home.html',student)
    

def show_details(request,year):
    student= {'yr':year}
    return render(request,'enroll/show.html',student)
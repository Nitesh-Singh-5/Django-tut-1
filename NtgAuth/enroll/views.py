from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUp,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm=SignUp(request.POST)
        if fm.is_valid():
            messages.add_message(request, messages.SUCCESS,'Your Account has been Created')
            fm.save()
            
    else:
        fm=SignUp()
    return render(request,'enroll/signup.html',{'form':fm})

# User Login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password= upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile/')
                    messages.success(request, 'account successfully login')
        else:
            fm=AuthenticationForm()
        return render(request,'enroll/userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

# User Profile
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm= EditAdminProfileForm(request.POST, instance=request.user)
                users= User.objects.all()
            else:
                fm= EditUserProfileForm(request.POST,instance=request.user)
                users = None
            if fm.is_valid():
                messages.success(request,'Profile Updated !!')
                fm.save()
        else:
            if request.user.is_superuser == True:  
                fm = EditAdminProfileForm(instance=request.user)
                users= User.objects.all()   
            else:
                fm=EditUserProfileForm(instance=request.user)
                users =None
        return render(request,'enroll/profile.html',{'name':request.user.username,'form':fm,'users':users})
    else:
        return HttpResponseRedirect('/login/')

# User Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# Change password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm=PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,'password successfully changed')
                return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request,'enroll/changepass.html',{'form':fm})
    else:
        HttpResponseRedirect('/login/')


# User details through admin panel
def user_detail(request,id):
    if request.user.is_authenticated:
        pi= User.objects.get(pk=id)
        fm= EditAdminProfileForm(instance=pi)
        return render(request,'enroll/profile.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')




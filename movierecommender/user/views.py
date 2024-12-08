from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def homepage(request):
    return render (request,'home.html')

def loginpage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login') 
    return render (request,'login.html')

def signuppage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        my_user=User.objects.create_user(uname,email,password)
        my_user.save()
        return redirect('login')
    return render (request,'signup.html')

def logoutpage(request):
    logout(request)
    return redirect('login')
    

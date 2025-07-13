from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')

def HomePage(request):
    return render (request, 'home.html')

def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is Incorrect!!!")
    return render (request, 'login.html')

def Registration(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
             return HttpResponse("Your password and confirm password are not same")
        else:
          
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

        print(uname,email,pass1,pass2)
    return render (request, 'registration.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
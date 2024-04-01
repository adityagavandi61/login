from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from dataapp.models import *
from django.contrib.auth.decorators import login_required
from dataapp.emailhandle import EmailHandle

# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def dologin(request):
    if request.method == 'POST':
        user = EmailHandle.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')

    else:
        return render(request, 'signin.html')

    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        profilepic=request.FILES.get('profilepic')

        if User.objects.filter(username=username).exists():
            messages.warning(request,'username is already taken')
            return redirect('register')
        else:
            user=User(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
            )
            user.set_password(password)
            user.save()
            profile=Profile(
                user=user,
                profilepic=profilepic,
            )
            profile.save()
            return redirect('dashboard')

    return render(request,'register.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
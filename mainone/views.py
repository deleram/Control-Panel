from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login as auth_login , logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

def login(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request, username=username , password=password)
        if user is not None:
            auth_login(request , user)
            videos=Videos.objects.all()
            context={'videos':videos}
            return render(request , 'mainone/teacher.html', context)
        else:
            messages.info(request , 'Username or password is wrong')

    return render(request, 'mainone/login.html')


def logingout(request):
    logout(request)
    return redirect(login)

@login_required(login_url='login')
def teacher(request):
    videos=Videos.objects.all()
    context={'videos':videos}
    return render(request, 'mainone/teacher.html',context)

def teacherexam(request):
    return render(request, 'mainone/teacherexam.html')


def teachervid(request):
    return render(request, 'mainone/teachervid.html')


@login_required(login_url='login')
def student(request):
    videos=Videos.objects.all()
    context={'videos':videos}
    return render(request, 'mainone/student.html',context)

def studentexam(request):
    return render(request, 'mainone/studentexam.html')

def studentvid(request):
    return render(request, 'mainone/studentvid.html')

@login_required(login_url='login')
def video(request,pk):
    video=Videos.objects.get(id=pk)
    contexts={'video' : video}
    return render(request,'mainone/video.html' , contexts)
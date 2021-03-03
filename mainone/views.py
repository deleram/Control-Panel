from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def login(request):
    return render(request, 'mainone/login.html')

def teacher(request):
    return render(request, 'mainone/teacher.html')


def teacherexam(request):
    return render(request, 'mainone/teacherexam.html')


def teachervid(request):
    return render(request, 'mainone/teachervid.html')



def student(request):
    videos=Videos.objects.all()
    context={'videos':videos}
    return render(request, 'mainone/student.html',context)

def studentexam(request):
    return render(request, 'mainone/studentexam.html')

def studentvid(request):
    return render(request, 'mainone/studentvid.html')


def video(request,pk):
    video=Videos.objects.get(id=pk)
    contexts={'video' : video}
    return render(request,'mainone/video.html' , contexts)
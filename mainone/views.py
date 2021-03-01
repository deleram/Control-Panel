from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'mainone/login.html')

def teacher(request):
    return render(request, 'mainone/teacher.html')


def teacherexam(request):
    return render(request, 'mainone/teacherexam.html')


def teachervid(request):
    return render(request, 'mainone/teachervid.html')



def student(request):
    return render(request, 'mainone/student.html')

def studentexam(request):
    return render(request, 'mainone/studentexam.html')

def studentvid(request):
    return render(request, 'mainone/studentvid.html')
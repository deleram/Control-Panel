from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login as auth_login , logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .decorator import *
import datetime


def login(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request, username=username , password=password)
        if user is not None:
            auth_login(request , user)
            return redirect('teacher')
        else:
            messages.info(request , 'Username or password is wrong')

    return render(request, 'mainone/login.html')


def logingout(request):
    logout(request)
    return redirect(login)

@login_required(login_url='login')
@admin_only
def teacher(request):
    videos=Videos.objects.all()
    assign=Assignment.objects.all()
    context={'videos':videos , 'assign':assign}
    if request.method == "POST"  :
        if request.POST.get("form_type") == 'form1':
            file2 = request.FILES["file"]
            caption = request.POST['caption']
            document = Videos.objects.create(name_of_the_video=caption ,vid=file2)

        else:
            deadline1= request.POST["deadline"]
            description1= request.POST["description"]
            number= request.POST["number"]
            assigning= Assignment.objects.create(number_of_the_assignment=number , assignment_description=description1 , deadline=deadline1)
            studentexercise=studentexercises.objects.create(numberexcer=number, des=description1 )
    return render(request, 'mainone/teacher.html',context)

def teacherexam(request):
    return render(request, 'mainone/teacherexam.html')


def teachervid(request):
    return render(request, 'mainone/teachervid.html')


@login_required(login_url='login')
def student(request):
    videos=Videos.objects.all()
    assigned=studentexercises.objects.all()
    context={'videos':videos , 'assigned':assigned}
    return render(request, 'mainone/student.html',context)

def studentexam(request,pk):
    assingn=studentexercises.objects.get(id=pk)
    contexts1={'assingn' : assingn}
    if request.method == "POST"  :
        exerfile = request.FILES["exerfile"]
        studentexercises.objects.filter(id = pk).update(exercise=exerfile , time=datetime.datetime.now() , studentname=User.first_name)


    return render(request, 'mainone/studentexam.html',contexts1)

def studentvid(request):
    return render(request, 'mainone/studentvid.html')

@login_required(login_url='login')
def video(request,pk):
    video=Videos.objects.get(id=pk)
    contexts={'video' : video}
    return render(request,'mainone/video.html' , contexts)
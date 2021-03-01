from django.urls import path
from . import views
urlpatterns = [
    path('', views.login),
    path('teacher/', views.teacher),
    path('student/', views.student),
    path('studentex/', views.studentexam),
    path('studentvid/', views.studentvid),
    path('teacherex/', views.teacherexam),
    path('teachervid/', views.teachervid)
]

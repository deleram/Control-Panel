from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . models import *
urlpatterns = [
    path('', views.login , name='login'),
    path('logout/' , views.logingout, name="logout"),
    path('teacher/', views.teacher, name='teacher'),
    path('student/', views.student, name="student"),
    path('studentex/<str:pk>', views.studentexam, name="studentex"),
    path('studentvid/', views.studentvid),
    path('teacherex/', views.teacherexam),
    path('video/<str:pk>', views.video , name='video')
]


if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
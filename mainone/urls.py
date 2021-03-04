from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.login , name='login'),
    path('logout/' , views.logingout, name="logout"),
    path('teacher/', views.teacher),
    path('student/', views.student),
    path('studentex/', views.studentexam),
    path('studentvid/', views.studentvid),
    path('teacherex/', views.teacherexam),
    path('teachervid/', views.teachervid),
    path('video/<str:pk>', views.video , name='video')
]


if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
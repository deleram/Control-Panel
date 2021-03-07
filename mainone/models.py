from django.db import models
from django.contrib.auth.models import User

class Assignment(models.Model):
    number_of_the_assignment=models.IntegerField()
    assignment_description = models.TextField()
    deadline=models.DateField()

    def __str__(self):
        return "Assignment " + str(self.number_of_the_assignment)

class Videos(models.Model):
    name_of_the_video=models.TextField(max_length=30)
    vid=models.FileField(upload_to='media', null=True)

class UserProfile(models.Model):
   user = models.OneToOneField(User , on_delete=models.CASCADE)
   student_number = models.CharField(max_length=256, blank=True, null=True)


class studentexercises(models.Model):
    des=models.TextField(null=True)
    numberexcer=models.IntegerField(null=True)
    exercise=models.FileField(upload_to='media', null=True , blank=True)
    time=models.DateField(null=True)
    score=models.IntegerField(range(0,100), null=True , blank=True , unique=True)
    studentname=models.CharField(max_length=256, blank=True , null=True)
    def __str__(self):
        return str(self.studentname) + str(self.numberexcer)






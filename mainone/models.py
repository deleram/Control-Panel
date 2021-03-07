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




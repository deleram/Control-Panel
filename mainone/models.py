from django.db import models


class Assignment(models.Model):
    number_of_the_assignment=models.IntegerField()
    assignment_description = models.TextField()
    deadline=models.DateField()

    def __str__(self):
        return "Assignment " + str(self.number_of_the_assignment)

class Videos(models.Model):
    name_of_the_video=models.TextField(max_length=30)
    vid=models.FileField(upload_to='mainone/media', null=True)



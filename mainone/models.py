from django.db import models


class test(models.Model):
    number_of_the_exam=models.IntegerField()
    exam_description = models.TextField()
    dead_line=models.DateField()

    def __str__(self):
        return "test " + str(self.number_of_the_exam)
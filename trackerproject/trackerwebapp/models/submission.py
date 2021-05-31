from django.db import models
from .classroom import Classroom
from .student import Student

class Submission(models.Model):

    time_submitted = models.DateTimeField()
    quiz_name = models.CharField(max_length=256)
    score = models.CharField(max_length=8)
    student = models.ForeignKey(
        Student,
        related_name='submissions',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

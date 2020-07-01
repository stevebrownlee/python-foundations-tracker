from django.db import models
from .classroom import Classroom
from .student import Student

class Submission(models.Model):

    time_submitted = models.DateTimeField()
    teacher_url = models.CharField(max_length=256)
    student_url = models.CharField(max_length=256)
    exercise = models.CharField(max_length=256)
    student = models.ForeignKey(
        Student,
        related_name='students',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    classroom = models.ForeignKey(
        Classroom,
        related_name='classrooms',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
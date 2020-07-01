from django.db import models

class Student(models.Model):

    PROGRAM_CHOICES = [
        ('FTWD', 'Full Time Web Development'),
        ('PTWD', 'Part Time Web Development'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    replit_id = models.IntegerField()
from django.db import models
from .cohort import Cohort

class Student(models.Model):

    PROGRAM_CHOICES = [
        ('FTWD', 'Full Time Web Development'),
        ('PTWD', 'Part Time Web Development'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    replit_id = models.IntegerField()
    cohort = models.ForeignKey(
        Cohort,
        related_name='students',
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.cohort.name)
from django.db import models
from .cohort import Cohort

class Student(models.Model):

    full_name = models.CharField(max_length=100)
    withdrawn = models.BooleanField(default=False, null=True, blank=True)
    withdrawn_date = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return self.full_name
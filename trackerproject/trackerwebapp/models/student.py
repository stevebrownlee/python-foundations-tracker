from django.db import models
from .cohort import Cohort

class Student(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    replit_id = models.IntegerField()
    withdrawn = models.BooleanField(default=False, null=True, blank=True)
    withdrawn_date = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
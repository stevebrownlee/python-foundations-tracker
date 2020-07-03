from django.db import models
from .cohort import Cohort

class Student(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    replit_id = models.IntegerField()
    withdrawn = models.BooleanField(default=False, null=True, blank=True)
    withdrawn_date = models.DateField(default=None, null=True, blank=True)
    second_chance_cohort = models.ForeignKey(
        Cohort,
        related_name='rollover_students',
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
    cohort = models.ForeignKey(
        Cohort,
        related_name='students',
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.cohort.name)
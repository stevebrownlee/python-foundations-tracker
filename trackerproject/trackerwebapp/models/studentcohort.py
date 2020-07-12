import datetime
from django.db import models

class StudentCohort(models.Model):

    student = models.ForeignKey("Student",
                                on_delete=models.DO_NOTHING,
                                blank=True,
                                null=True,
                                related_name="studentcohorts")

    cohort = models.ForeignKey("Cohort",
                               on_delete=models.DO_NOTHING,
                               blank=True,
                               null=True,
                               related_name="studentcohorts")

    timestamp = models.DateField(default=datetime.date.today, null=True, blank=True)
    initial = models.BooleanField(default=False, null=True, blank=True)

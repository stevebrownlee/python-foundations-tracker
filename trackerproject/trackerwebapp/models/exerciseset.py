from django.db import models

class ExerciseSet(models.Model):

    title = models.CharField(max_length=100)

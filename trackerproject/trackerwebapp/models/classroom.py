from django.db import models

class Classroom(models.Model):

    title = models.CharField(max_length=100)

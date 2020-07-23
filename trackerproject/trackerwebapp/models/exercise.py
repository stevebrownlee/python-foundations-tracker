from django.db import models
from .language import Language


class Exercise(models.Model):

    title = models.CharField(max_length=100)
    language = models.ForeignKey(
        Language, blank=True, null=True, on_delete=models.DO_NOTHING)

from django.db import models

class ResourceType(models.Model):

    label = models.CharField(max_length=100)

from django.db import models

class Resource(models.Model):

    title = models.CharField(max_length=100)
    resource_type = models.ForeignKey("ResourceType",
                               on_delete=models.DO_NOTHING,
                               blank=False,
                               null=False,
                               related_name="resources")

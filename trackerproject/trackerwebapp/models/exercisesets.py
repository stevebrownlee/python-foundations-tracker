from django.db import models

class ExercisesSets(models.Model):

    exercise = models.ForeignKey("Exercise",
                               on_delete=models.DO_NOTHING,
                               blank=False,
                               null=False,
                               related_name="exercise_set_relationships")
    exerciseset = models.ForeignKey("ExerciseSet",
                               on_delete=models.DO_NOTHING,
                               blank=False,
                               null=False,
                               related_name="exercise_set_relationships")

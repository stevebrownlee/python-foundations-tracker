from trackerwebapp.models.exercisesets import ExercisesSets
from django.contrib import admin

# Register your models here.
from trackerwebapp.models import Cohort, Student, StudentCohort
from trackerwebapp.models import Language, Exercise
from trackerwebapp.models import ExerciseSet, ExercisesSets
from trackerwebapp.models import Resource, ResourceType


class ExerciseSetsAdmin(admin.ModelAdmin):
    pass


class StudentCohortAdmin(admin.ModelAdmin):
    pass


class ResourceAdmin(admin.ModelAdmin):
    pass


class ResourceTypeAdmin(admin.ModelAdmin):
    pass


class CohortAdmin(admin.ModelAdmin):
    pass


class LanguageAdmin(admin.ModelAdmin):
    pass


class ExerciseAdmin(admin.ModelAdmin):
    pass


class ExerciseSetAdmin(admin.ModelAdmin):
    pass


class ExercisesSetsAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cohort, CohortAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(ExerciseSet, ExerciseSetAdmin)
admin.site.register(ExercisesSets, ExercisesSetsAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(ResourceType, ResourceTypeAdmin)

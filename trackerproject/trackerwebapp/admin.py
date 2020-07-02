from django.contrib import admin

# Register your models here.
from trackerwebapp.models import Cohort, Student

class CohortAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cohort, CohortAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)
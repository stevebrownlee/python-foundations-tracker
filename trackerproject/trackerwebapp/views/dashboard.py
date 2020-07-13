from django.db.models import Count
from django.shortcuts import render
from ..models import Submission, Student, Cohort

def dashboard(request):
    if request.method == 'GET':

        cohorts = Cohort.objects.all() \
            .annotate(student_count=Count('studentcohorts__student')) \
            .order_by('-name')

        template = 'dashboard.html'
        context = {
            'cohorts': cohorts
        }

        return render(request, template, context)
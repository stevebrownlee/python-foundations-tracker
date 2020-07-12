from django.shortcuts import render, redirect
from django.urls import reverse
from ...models import Student, Cohort

def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all().order_by('-id')
        cohorts = Cohort.objects.all().order_by('-name')


        template = 'student_list.html'
        context = {
            'students': students,
            'cohorts': cohorts,
        }

        return render(request, template, context)
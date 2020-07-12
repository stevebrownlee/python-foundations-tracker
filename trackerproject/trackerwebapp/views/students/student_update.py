from django.shortcuts import render, redirect
from django.urls import reverse
from ...models import Student, Cohort, StudentCohort

def student_update(request):
    if request.method == 'POST':
        cohort = request.POST.get('cohort', None)
        student = request.POST.get('student', None)

        transfer = StudentCohort()
        transfer.student = student
        transfer.cohort = cohort
        transfer.initial = True
        transfer.save()

        return redirect(reverse('student_report', kwargs={'student_id': student}))

def quick_student_update(request):
    if request.method == 'POST':
        redirect_to = request.POST.get('view')
        cohort = request.POST.get('cohortSelect', None)
        student = request.POST.get('student', None)

        cohort = request.POST.get('cohort', None)
        student = request.POST.get('student', None)

        transfer = StudentCohort()
        transfer.student = student
        transfer.cohort = cohort
        transfer.initial = True
        transfer.save()

        return redirect(reverse(redirect_to))

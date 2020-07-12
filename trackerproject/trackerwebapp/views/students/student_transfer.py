from datetime import date
from django.shortcuts import render, redirect
from django.urls import reverse
from ...models import Student, Cohort, StudentCohort


def student_transfer(request):
    if request.method == 'POST':
        new_cohort = request.POST.get('transfer_cohort', None)
        cohort = Cohort.objects.get(pk=new_cohort)

        student_id = request.POST.get('student', None)
        student = Student.objects.get(pk=student_id)

        transfer = StudentCohort()
        transfer.student = student
        transfer.cohort = cohort
        transfer.save()

        return redirect(reverse('student_report', kwargs={'student_id': student_id}))


from datetime import date
from django.shortcuts import render, redirect
from django.urls import reverse
from ...models import Student, Cohort, StudentCohort


def student_transfer(request):
    if request.method == 'POST':
        new_cohort = request.POST.get('transfer_cohort', None)
        student_id = request.POST.get('student', None)

        student = Student.objects.get(pk=student_id)

        if new_cohort == "reset":
            try:
                transfer = StudentCohort.objects.get(
                    student=student, initial=False).delete()
            except StudentCohort.DoesNotExist:
                pass

        elif new_cohort != "0":
            cohort = Cohort.objects.get(pk=new_cohort)

            try:
                existing = StudentCohort.objects.get(cohort=cohort, student=student)
            except StudentCohort.DoesNotExist:
                transfer = StudentCohort()
                transfer.student = student
                transfer.cohort = cohort
                transfer.initial = False
                transfer.save()

        return redirect(reverse('student_report', kwargs={'student_id': student_id}))

from datetime import date
from django.shortcuts import render, redirect
from django.urls import reverse
from ..models import Student, Cohort


def student_withdrawal(request):
    if request.method == 'POST':
        withdrawal = request.POST.get('withdrawal', None)
        student_id = request.POST.get('student', None)
        student = Student.objects.get(pk=student_id)

        student.withdrawn = True
        student.withdrawn_date = date.today()

        if withdrawal == "null":
            student.second_chance_cohort = None
        else:
            student.second_chance_cohort = Cohort.objects.get(pk=withdrawal)

        student.save()

        return redirect(reverse('student_report', kwargs={'student_id': student_id}))


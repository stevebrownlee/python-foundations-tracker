from django.shortcuts import render, redirect
from django.urls import reverse
from ..models import Student, Cohort

def update(student_id, cohort):
    student = Student.objects.get(pk=student_id)
    student.cohort = Cohort.objects.get(pk=cohort)
    student.save()


def student_update(request):
    if request.method == 'POST':
        cohort = request.POST.get('cohort', None)
        student_id = request.POST.get('student', None)
        update(student_id, cohort)

        return redirect(reverse('student_report', kwargs={'student_id': student_id}))

def quick_student_update(request):
    if request.method == 'POST':
        redirect_to = request.POST.get('view')
        cohort = request.POST.get('cohortSelect', None)
        student_id = request.POST.get('student', None)
        update(student_id, cohort)

        return redirect(reverse(redirect_to))

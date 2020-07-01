from django.shortcuts import render, redirect
from django.urls import reverse
from ..models import Submission, Student

def student_update(request):
    if request.method == 'POST':
        cohort = request.POST.get('cohort', None)
        student_id = request.POST.get('student', None)

        student = Student.objects.get(pk=student_id)
        student.cohort = cohort
        student.save()

        return redirect(reverse('student_report', kwargs={'student_id': student_id}))
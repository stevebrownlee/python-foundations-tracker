from django.shortcuts import render
from ..models import Submission, Student

def student_report(request, student_id):
    if request.method == 'GET':
        student = Student.objects.get(pk=student_id)
        submissions = Submission.objects.filter(student=student)
        submissions.order_by('exercise')

        template = 'report.html'
        context = {
            'student': student,
            'submissions': submissions,
        }

        return render(request, template, context)
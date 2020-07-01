from django.shortcuts import render
from ..models import Submission

def submission_list(request):
    if request.method == 'GET':
        all_submissions = Submission.objects.all()

        template = 'submissions.html'
        context = {
            'all_submissions': all_submissions
        }

        return render(request, template, context)
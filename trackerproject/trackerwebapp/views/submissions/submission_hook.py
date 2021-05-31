import json
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from ...models import Student, Submission

@require_POST
@csrf_exempt
def submission(request):
    sub = json.loads(request.body.decode("utf-8"))
    print(sub)

    try:
        student = Student.objects.get(full_name=sub['submissionData']['Your name'][0])
    except Student.DoesNotExist:
        student = Student()
        student.full_name = sub['submissionData']['Your name'][0]
        student.save()
        print(student)

    try:
        already_recorded = Submission.objects.get(student=student, quiz_name=sub['formName'])
    except Submission.DoesNotExist:
        print("Submission does not exists. Creating...")
        submission = Submission()
        submission.time_submitted = sub['submissionData']['Timestamp'][0]
        submission.quiz_name = sub['formName']
        submission.score = sub['submissionData']['Score'][0]
        submission.student = student
        submission.save()
        print(submission)

    return HttpResponse('Thank you')
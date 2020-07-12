import json
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from ...models import Student, Classroom, Submission

@require_POST
@csrf_exempt
def submission(request):
    sub = json.loads(request.body.decode("utf-8"))
    print(sub)

    try:
        student = Student.objects.get(replit_id=sub['student']['id'])
    except Student.DoesNotExist:
        student = Student()
        student.first_name = sub['student']['first_name']
        student.last_name = sub['student']['last_name']
        student.replit_id = sub['student']['id']
        student.save()

    try:
        classroom = Classroom.objects.get(replit_id=sub['classroom']['id'])
    except Classroom.DoesNotExist:
        classroom = Classroom()
        classroom.replit_id = sub['classroom']['id']
        classroom.title = sub['classroom']['name']
        classroom.save()

    if sub['submission']['status'] == "complete":
        try:
            already_recorded = Submission.objects.get(student=student, classroom=classroom, exercise=sub['assignment']['name'])
        except Submission.DoesNotExist:
            submission = Submission()
            submission.time_submitted = sub['submission']['time_submitted']
            submission.teacher_url = sub['submission']['teacher_url']
            submission.student_url = sub['submission']['student_url']
            submission.exercise = sub['assignment']['name']
            submission.student = student
            submission.classroom = classroom
            submission.save()

    return HttpResponse('Thank you')
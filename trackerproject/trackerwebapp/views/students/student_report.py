from django.shortcuts import render
from ...models import Submission, Student, Cohort, StudentCohort

VARIABLES_INTRO_CLASSROOM_EXERCISES = 7
ARRAYS_INTRO_CLASSROOM_EXERCISES = 11
OBJECTS_INTRO_CLASSROOM_EXERCISES = 7
FUNCTION_INTRO_CLASSROOM_EXERCISES = 15
FUNCTION_CLASSROOM_EXERCISES = 6
ITERATION_CLASSROOM_EXERCISES = 7
CONDITIONS_CLASSROOM_EXERCISES = 5

def student_report(request, student_id):
    if request.method == 'GET':
        iteration_exercises = set()
        condition_exercises = set()
        function_exercises = set()
        functions_intro_exercises = set()
        variables_intro_exercises = set()
        iteration_intro_exercises = set()
        objects_intro_exercises = set()

        student = Student.objects.get(pk=student_id)
        submissions = Submission.objects.filter(student=student)
        cohort_history = StudentCohort.objects.filter(student=student)

        student_assigned_cohort = StudentCohort.objects.filter(student=student, initial=True).first()

        submissions.order_by('classroom')
        for submission in submissions:
            if submission.classroom.title == 'Iteration with JavaScript':
                iteration_exercises.add(submission.exercise)
            if submission.classroom.title == 'JavaScript Conditions':
                condition_exercises.add(submission.exercise)
            if submission.classroom.title == 'JavaScript Functions':
                function_exercises.add(submission.exercise)
            if submission.classroom.title == 'Introduction to Functions':
                functions_intro_exercises.add(submission.exercise)
            if submission.classroom.title == 'Introduction to JavaScript Variables':
                variables_intro_exercises.add(submission.exercise)
            if submission.classroom.title == 'Introduction to Arrays and Iteration':
                iteration_intro_exercises.add(submission.exercise)
            if submission.classroom.title == 'Introduction to Objects':
                objects_intro_exercises.add(submission.exercise)

        scores = {}
        scores['function_percent'] = len(function_exercises) / FUNCTION_CLASSROOM_EXERCISES * 100
        scores['iteration_percent'] = len(iteration_exercises) / ITERATION_CLASSROOM_EXERCISES * 100
        scores['condition_percent'] = len(condition_exercises) / CONDITIONS_CLASSROOM_EXERCISES * 100

        scores['intro_functions_percent'] = len(functions_intro_exercises) / FUNCTION_INTRO_CLASSROOM_EXERCISES * 100
        scores['intro_iteration_percent'] = len(iteration_intro_exercises) / ARRAYS_INTRO_CLASSROOM_EXERCISES * 100
        scores['intro_objects_percent'] = len(objects_intro_exercises) / OBJECTS_INTRO_CLASSROOM_EXERCISES * 100
        scores['intro_variables_percent'] = len(variables_intro_exercises) / VARIABLES_INTRO_CLASSROOM_EXERCISES * 100

        submissions.order_by('time_submitted')

        cohorts = Cohort.objects.all().order_by('name')


        template = 'report.html'
        context = {
            'student': student,
            'submissions': submissions,
            'scores': scores,
            'cohorts': cohorts,
            'cohort_history': cohort_history,
            'student_assigned_cohort': student_assigned_cohort,
        }

        return render(request, template, context)
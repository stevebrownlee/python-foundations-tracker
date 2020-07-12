from django.shortcuts import render
from ...models import Submission, Student, Cohort

VARIABLES_INTRO_CLASSROOM_EXERCISES = 7
ARRAYS_INTRO_CLASSROOM_EXERCISES = 11
OBJECTS_INTRO_CLASSROOM_EXERCISES = 7
FUNCTION_INTRO_CLASSROOM_EXERCISES = 15
FUNCTION_CLASSROOM_EXERCISES = 6
ITERATION_CLASSROOM_EXERCISES = 7
CONDITIONS_CLASSROOM_EXERCISES = 5

def cohort_report(request, cohort_id):
    if request.method == 'GET':

        cohort = Cohort.objects.get(pk=cohort_id)
        students = Student.objects.filter(cohort=cohort)
        student_summaries = []

        for student in students:

            student_data = {}
            iteration_exercises = set()
            condition_exercises = set()
            function_exercises = set()
            functions_intro_exercises = set()
            variables_intro_exercises = set()
            iteration_intro_exercises = set()
            objects_intro_exercises = set()

            submissions = Submission.objects.filter(student=student)
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

            student_data['student'] = student
            student_data['scores'] = {}
            student_data['scores']['function_percent'] = len(function_exercises) / FUNCTION_CLASSROOM_EXERCISES * 100
            student_data['scores']['iteration_percent'] = len(iteration_exercises) / ITERATION_CLASSROOM_EXERCISES * 100
            student_data['scores']['condition_percent'] = len(condition_exercises) / CONDITIONS_CLASSROOM_EXERCISES * 100

            student_data['scores']['intro_functions_percent'] = len(functions_intro_exercises) / FUNCTION_INTRO_CLASSROOM_EXERCISES * 100
            student_data['scores']['intro_iteration_percent'] = len(iteration_intro_exercises) / ARRAYS_INTRO_CLASSROOM_EXERCISES * 100
            student_data['scores']['intro_objects_percent'] = len(objects_intro_exercises) / OBJECTS_INTRO_CLASSROOM_EXERCISES * 100
            student_data['scores']['intro_variables_percent'] = len(variables_intro_exercises) / VARIABLES_INTRO_CLASSROOM_EXERCISES * 100
            student_data['completion_percentage'] = (student_data['scores']['function_percent'] +
                student_data['scores']['iteration_percent'] +
                student_data['scores']['condition_percent'] +
                student_data['scores']['intro_functions_percent'] +
                student_data['scores']['intro_iteration_percent'] +
                student_data['scores']['intro_objects_percent'] +
                student_data['scores']['intro_variables_percent']) / 7

            student_summaries.append(student_data)

        student_summaries.sort(key=lambda s: s['completion_percentage'], reverse=True)
        template = 'cohort_report.html'
        context = {
            'student_summaries': student_summaries,
            'cohort': cohort,
        }

        return render(request, template, context)
import csv
from datetime import date
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from ..models import Student, Classroom, Submission


WEDDING = "Wedding Function"
JOURNAL = "Making a journal entry component"
HIGHER_ORDER = "Functions calling functions"
PARAMETERS = "Function Parameters and Arguments"
CAR_FACTORY = "Car Factory Functions"
STUDENT_ASSIGNMENTS = "Student Assignments"

ASSIGNMENTS = [WEDDING, JOURNAL, HIGHER_ORDER, PARAMETERS, CAR_FACTORY, STUDENT_ASSIGNMENTS]


def create_submission(student, classroom, exercise):
    submission = Submission()
    submission.time_submitted = date.today()
    submission.teacher_url = ''
    submission.student_url = ''
    submission.exercise = exercise
    submission.student = student
    submission.classroom = classroom
    submission.save()


def import_functions(request):
    with open('/home/steve/foundations-tracker/trackerproject/trackerwebapp/imports/JavaScript_Functions.csv', 'r') as students_file:
        students = csv.reader(students_file)

        for _student in students:
            record = {}
            record['student_id'] = _student[0]
            record['name'] = "{} {}".format(_student[2], _student[3])
            record[WEDDING] = _student[5]
            record[JOURNAL] = _student[6]
            record[HIGHER_ORDER] = _student[7]
            record[PARAMETERS] = _student[8]
            record[CAR_FACTORY] = _student[9]
            record[STUDENT_ASSIGNMENTS] = _student[10]

            try:
                student = Student.objects.get(replit_id=int(record['student_id']))
            except Student.DoesNotExist:
                student = Student()
                student.first_name = _student[2]
                student.last_name = _student[3]
                student.replit_id = record['student_id']
                student.save()

            classroom = Classroom.objects.get(title='JavaScript Functions')

            for assignment in ASSIGNMENTS:
                if record[assignment] == 'complete':
                    already_recorded = Submission.objects.filter(student=student, classroom=classroom, exercise=assignment).first()
                    if already_recorded is None:
                        create_submission(student, classroom, assignment)

    return HttpResponse('Complete')

def import_iteration(request):
    assignments = ['Simple iteration of a collection','Building a sentence','Using the Power of of','Nested loops','Adults only','Using iteration to filter a collection','Using iteration to create a new collection']
    with open('/home/steve/foundations-tracker/trackerproject/trackerwebapp/imports/Iteration_with_JavaScript.csv', 'r') as students_file:
        students = csv.reader(students_file)

        for _student in students:
            record = {}
            record['Simple iteration of a collection'] = _student[5]
            record['Building a sentence'] = _student[6]
            record['Using the Power of of'] = _student[7]
            record['Nested loops'] = _student[8]
            record['Adults only'] = _student[9]
            record['Using iteration to filter a collection'] = _student[10]
            record['Using iteration to create a new collection'] = _student[11]

            try:
                student = Student.objects.get(replit_id=int(_student[0]))
            except Student.DoesNotExist:
                student = Student()
                student.first_name = _student[2]
                student.last_name = _student[3]
                student.replit_id = _student[0]
                student.save()

            classroom = Classroom.objects.get(title='Iteration with JavaScript')

            for assignment in assignments:
                if record[assignment] == 'complete':
                    already_recorded = Submission.objects.filter(student=student, classroom=classroom, exercise=assignment).first()
                    if already_recorded is None:
                        create_submission(student, classroom, assignment)

    return HttpResponse('Complete')

def import_conditions(request):
    assignments = ['Single Conditions','Multiple Conditions','Switch Statement','Nested Conditions','Challenge!']
    with open('/home/steve/foundations-tracker/trackerproject/trackerwebapp/imports/JavaScript_Conditions.csv', 'r') as students_file:
        students = csv.reader(students_file)

        for _student in students:
            record = {}
            record['Single Conditions'] = _student[5]
            record['Multiple Conditions'] = _student[6]
            record['Switch Statement'] = _student[7]
            record['Nested Conditions'] = _student[8]
            record['Challenge!'] = _student[9]

            try:
                student = Student.objects.get(replit_id=int(_student[0]))
            except Student.DoesNotExist:
                student = Student()
                student.first_name = _student[2]
                student.last_name = _student[3]
                student.replit_id = _student[0]
                student.save()

            classroom = Classroom.objects.get(title='JavaScript Conditions')

            for assignment in assignments:
                if record[assignment] == 'complete':
                    already_recorded = Submission.objects.filter(student=student, classroom=classroom, exercise=assignment).first()
                    if already_recorded is None:
                        create_submission(student, classroom, assignment)

    return HttpResponse('Complete')

def import_intro_variables(request):
    assignments = ['Part 1: Variables and Values','Part 2: String Values in Variables','Part 3: "Scary" Math with Variables','Part 4: Multi-line Strings','Part 5: Ill Logical Variables','Review: Variables','Part 6: More or Less Party']
    with open('/home/steve/foundations-tracker/trackerproject/trackerwebapp/imports/Introduction_to_JavaScript_Variables.csv', 'r') as students_file:
        students = csv.reader(students_file)

        for _student in students:
            record = {}
            record['Part 1: Variables and Values'] = _student[5]
            record['Part 2: String Values in Variables'] = _student[6]
            record['Part 3: "Scary" Math with Variables'] = _student[7]
            record['Part 4: Multi-line Strings'] = _student[8]
            record['Part 5: Ill Logical Variables'] = _student[9]
            record['Review: Variables'] = _student[10]
            record['Part 6: More or Less Party'] = _student[11]

            try:
                student = Student.objects.get(replit_id=int(_student[0]))
            except Student.DoesNotExist:
                student = Student()
                student.first_name = _student[2]
                student.last_name = _student[3]
                student.replit_id = _student[0]
                student.save()

            classroom = Classroom.objects.get(title='Introduction to JavaScript Variables')

            for assignment in assignments:
                if record[assignment] == 'complete':
                    already_recorded = Submission.objects.filter(student=student, classroom=classroom, exercise=assignment).first()
                    if already_recorded is None:
                        create_submission(student, classroom, assignment)

    return HttpResponse('Complete')

def import_intro_arrays(request):
    assignments = ['Part 1: Cleaning the Dishes','Part 2: Programming Topics','Part 4: Fast Food Worker','Part 5: Yearly Grocery Costs','Part 6: Average Miles','Part 7: Sleep and Moods','Part 8: How Do You Like Your Coffee?','Review: Iteration','Introduction and Syntax','Part 9: Split Personalities','Part 3: The Hairy Potter']
    with open('/home/steve/foundations-tracker/trackerproject/trackerwebapp/imports/Introduction_to_Arrays_and_Iteration.csv', 'r') as students_file:
        students = csv.reader(students_file)

        for _student in students:
            record = {}
            record['Part 1: Cleaning the Dishes'] = _student[5]
            record['Part 2: Programming Topics'] = _student[6]
            record['Part 4: Fast Food Worker'] = _student[7]
            record['Part 5: Yearly Grocery Costs'] = _student[8]
            record['Part 6: Average Miles'] = _student[9]
            record['Part 7: Sleep and Moods'] = _student[10]
            record['Part 8: How Do You Like Your Coffee?'] = _student[11]
            record['Review: Iteration'] = _student[12]
            record['Introduction and Syntax'] = _student[13]
            record['Part 9: Split Personalities'] = _student[14]
            record['Part 3: The Hairy Potter'] = _student[15]

            try:
                student = Student.objects.get(replit_id=int(_student[0]))
            except Student.DoesNotExist:
                student = Student()
                student.first_name = _student[2]
                student.last_name = _student[3]
                student.replit_id = _student[0]
                student.save()

            classroom = Classroom.objects.get(title='Introduction to Arrays and Iteration')

            for assignment in assignments:
                if record[assignment] == 'complete':
                    already_recorded = Submission.objects.filter(student=student, classroom=classroom, exercise=assignment).first()
                    if already_recorded is None:
                        create_submission(student, classroom, assignment)

    return HttpResponse('Complete')

def import_intro_objects(request):
    assignments = ['Introduction and Syntax','Flower Shop','Doctor Office Schedule','Sales Associate','Librarian and the Book','GoldFish Tanks','Voting Booth']
    with open('/home/steve/foundations-tracker/trackerproject/trackerwebapp/imports/Introduction_to_Objects.csv', 'r') as students_file:
        students = csv.reader(students_file)

        for _student in students:
            record = {}
            record['Introduction and Syntax'] = _student[5]
            record['Flower Shop'] = _student[6]
            record['Doctor Office Schedule'] = _student[7]
            record['Sales Associate'] = _student[8]
            record['Librarian and the Book'] = _student[9]
            record['GoldFish Tanks'] = _student[10]
            record['Voting Booth'] = _student[11]

            try:
                student = Student.objects.get(replit_id=int(_student[0]))
            except Student.DoesNotExist:
                student = Student()
                student.first_name = _student[2]
                student.last_name = _student[3]
                student.replit_id = _student[0]
                student.save()

            classroom = Classroom.objects.get(title='Introduction to Objects')

            for assignment in assignments:
                if record[assignment] == 'complete':
                    already_recorded = Submission.objects.filter(student=student, classroom=classroom, exercise=assignment).first()
                    if already_recorded is None:
                        create_submission(student, classroom, assignment)

    return HttpResponse('Complete')

def import_intro_functions(request):
    assignments = ['Introduction and Syntax','Return to Sender','Deconstruction: Calculator','Deconstruction: Car Factory','Deconstruction: An Introduction','Deconstruction: Making Pottery for Profit','Deconstruction: Candy Treats','Converting Objects to Strings','Function Flow: Introduction','Function Flow: Add Then Multiply','Function Flow: Adding Properties','Function Flow: Candy','Paint the House','Storing Return Values','Storing Two Return Values']
    with open('/home/steve/foundations-tracker/trackerproject/trackerwebapp/imports/Introduction_to_Functions.csv', 'r') as students_file:
        students = csv.reader(students_file)

        for _student in students:
            record = {}
            record['Introduction and Syntax'] = _student[5]
            record['Return to Sender'] = _student[6]
            record['Deconstruction: Calculator'] = _student[7]
            record['Deconstruction: Car Factory'] = _student[8]
            record['Deconstruction: An Introduction'] = _student[9]
            record['Deconstruction: Making Pottery for Profit'] = _student[10]
            record['Deconstruction: Candy Treats'] = _student[11]
            record['Converting Objects to Strings'] = _student[12]
            record['Function Flow: Introduction'] = _student[13]
            record['Function Flow: Add Then Multiply'] = _student[14]
            record['Function Flow: Adding Properties'] = _student[15]
            record['Function Flow: Candy'] = _student[16]
            record['Paint the House'] = _student[17]
            record['Storing Return Values'] = _student[18]
            record['Storing Two Return Values'] = _student[19]

            try:
                student = Student.objects.get(replit_id=int(_student[0]))
            except Student.DoesNotExist:
                student = Student()
                student.first_name = _student[2]
                student.last_name = _student[3]
                student.replit_id = _student[0]
                student.save()

            classroom = Classroom.objects.get(title='Introduction to Functions')

            for assignment in assignments:
                if record[assignment] == 'complete':
                    already_recorded = Submission.objects.filter(student=student, classroom=classroom, exercise=assignment).first()
                    if already_recorded is None:
                        create_submission(student, classroom, assignment)

    return HttpResponse('Complete')
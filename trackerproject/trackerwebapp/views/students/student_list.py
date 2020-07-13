import sqlite3
from django.shortcuts import render
from ...models import Student, Cohort
import os



DB_PATH = "{}/db.sqlite3".format(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

def student_list(request):
    if request.method == 'GET':

        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    s.id,
                    s.first_name,
                    s.last_name,
                    c.name,
                    c.id as cohort_id,
                    sc.initial
                from trackerwebapp_student s
                left join trackerwebapp_studentcohort sc on sc.student_id = s.id
                left join trackerwebapp_cohort c on sc.cohort_id = c.id
                where sc.initial is not 0
                order by s.id desc
            """)

            all_students = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                student = Student()
                student.id = row['id']
                student.first_name = row['first_name']
                student.last_name = row['last_name']
                student.cohort_name = row['name']
                student.cohort_id = row['cohort_id']
                student.initial_cohort = row['initial']

                all_students.append(student)

        cohorts = Cohort.objects.all().order_by('-name')

        template = 'student_list.html'
        context = {
            'students': all_students,
            'cohorts': cohorts,
        }

        return render(request, template, context)

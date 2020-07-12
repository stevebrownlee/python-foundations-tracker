from django.shortcuts import render
from ...models import Submission, Cohort

def submission_list(request):
    if request.method == 'GET':
        order = request.GET.get('order_by', None)
        direction = request.GET.get('direction', None)

        all_submissions = Submission.objects.all().order_by('-time_submitted')
        all_cohorts = Cohort.objects.all().order_by('-name')

        if order is not None:
            if order == "student":
                order_filter = "student__last_name"
            else:
                order_filter = order

            if order == "cohort":
                order_filter = "student__cohort"
            else:
                order_filter = order

            if direction is not None:
                if direction == "desc":
                    order_filter = '-{}'.format(order_filter)

            all_submissions = all_submissions.order_by(order_filter)

        template = 'submissions.html'
        context = {
            'all_submissions': all_submissions[:50],
            'order': order,
            'all_cohorts': all_cohorts,
            'direction': direction
        }

        return render(request, template, context)
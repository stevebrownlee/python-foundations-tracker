from django.shortcuts import render
from ..models import Submission

def submission_list(request):
    if request.method == 'GET':
        order = request.GET.get('order_by', None)
        direction = request.GET.get('direction', None)

        all_submissions = Submission.objects.all()

        if order is not None:
            order_filter = order

            if direction is not None:
                if direction == "desc":
                    order_filter = '-{}'.format(order)

            all_submissions = all_submissions.order_by(order_filter)

        template = 'submissions.html'
        context = {
            'all_submissions': all_submissions
        }

        return render(request, template, context)
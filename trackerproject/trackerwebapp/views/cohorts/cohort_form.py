from django.shortcuts import render

def cohort_form(request):
    if request.method == 'GET':
        template = 'cohort_form.html'
        context = { }

        return render(request, template, context)
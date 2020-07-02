from django.shortcuts import render, redirect
from django.urls import reverse
from ..models import Cohort

def cohorts(request):
    if request.method == 'POST':
        cohort = Cohort()
        cohort.name = request.POST.get('name')
        cohort.save()

        return redirect(reverse('dashboard'))
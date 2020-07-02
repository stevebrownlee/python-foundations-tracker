"""trackerproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from trackerwebapp.models import *
from trackerwebapp.views import *

app_name = "tracker"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('cohort/form', cohort_form, name='cohort_form'),
    path('submission/', submission, name='submission_hook'),
    path('students/<int:student_id>/', student_report, name='student_report'),
    path('cohorts/', cohorts, name='cohorts'),
    path('cohorts/<int:cohort_id>/', cohort_report, name='cohort_report'),
    path('submissions/', submission_list, name='submission_list'),
    path('studentupdate/', student_update, name='student_update'),
    path('quickupdate/', quick_student_update, name='quick_student_update'),
]

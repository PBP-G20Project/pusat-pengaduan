from django.shortcuts import render, redirect
from submission_form.models import Report
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
#@login_required(login_url = '/login/')
def show_report(request):
    report_objects = Report.objects.filter(admin_submission = request.user)
    context = {
        "report": report_objects,
        "username": request.user}
    return render(request, "accusation.html", context)

def report_next(request):
    report_objects = Report.objects.filter(admin_submission = request.user, id=id)
    update_status_next(report_objects)

def report_prev(request):
    report_objects = Report.objects.filter(admin_submission = request.user, id=id)
    update_status_back(report_objects)

def report_reject(request):
    report_objects = Report.objects.filter(admin_submission = request.user, id=id)
    update_status_reject(report_objects)
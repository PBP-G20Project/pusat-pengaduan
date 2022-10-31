from django.shortcuts import render, redirect
from submission_form.models import Report
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
@login_required(login_url = '/login/')
def show_report(request):
    report_objects = Report.objects.filter(user_submission=request.user)
    context = {
        "report": report_objects,
        "username": request.user,
    }
    return render(request, "accusation.html", context)

@login_required(login_url = "/login/")
def update_diproses (request, id):
    report = Report.objects.get(user = request.user, id=id)
    report.diproses = not (report.diproses)
    report.save(update_fields = ["diproses"])
    return HttpResponseRedirect(reverse("dashboard_admin:show_report"))

@login_required(login_url='/login/')
def update_selesai (request, id):
    report = Report.objects.get(user = request.user, id=id)
    report.selesai = not (report.selesai)
    report.save(update_fields = ["selesai"])
    return HttpResponseRedirect(reverse("dashboard_admin:show_report"))


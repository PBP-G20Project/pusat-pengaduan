from django.shortcuts import render, redirect
from submission_form.models import Report
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse

# Create your views here.
@login_required(login_url = '/login/')
def show_report(request):
    if not request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    report_objects = Report.objects.filter(admin_submission = request.user)
    context = {
        "report": report_objects,
        "username": request.user,
    }
    return render(request, "accusation.html", context)


@login_required(login_url = '/login/')

def report_next(request, id):
    if not request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    report_objects = Report.objects.get(admin_submission = request.user, id=id)
    report_objects.update_status_next()
    report_objects.save(update_fields = ["status"])
    return HttpResponseRedirect(reverse("dashboard_admin:show_report"))

@login_required(login_url = '/login/')
def report_prev(request, id):
    if not request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    report_objects = Report.objects.get(admin_submission = request.user, id=id)
    report_objects.update_status_back()
    report_objects.save(update_fields = ["status"])
    return HttpResponseRedirect(reverse("dashboard_admin:show_report"))

@login_required(login_url = '/login/')
def report_reject(request, id):
    if not request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    report_objects = Report.objects.get(admin_submission = request.user, id=id)
    report_objects.update_status_reject()
    report_objects.save(update_fields = ["status"])
    return HttpResponseRedirect(reverse("dashboard_admin:show_report"))

def show_all_report(request):
    report_objects = Report.objects.filter(admin_submission = request.user)
    return HttpResponse(
        serializers.serialize('json', report_objects),
        content_type = 'application/json' 
        )

def show_all_pending(request):
    report_objects = Report.objects.filter(admin_submission = request.user, status = "PENDING")
    return HttpResponse(
        serializers.serialize('json', report_objects),
        content_type = 'application/json' 
        )

def show_all_diproses(request):
    report_objects = Report.objects.filter(admin_submission = request.user, status = "DIPROSES")
    return HttpResponse(
        serializers.serialize('json', report_objects),
        content_type = 'application/json' 
        )
        
def show_all_selesai(request):
    report_objects = Report.objects.filter(admin_submission = request.user, status = "SELESAI")
    return HttpResponse(
        serializers.serialize('json', report_objects),
        content_type = 'application/json' 
        )
def show_all_ditolak(request):
    report_objects = Report.objects.filter(admin_submission = request.user, status = "REJECTED")
    return HttpResponse(
        serializers.serialize('json', report_objects),
        content_type = 'application/json' 
        )

@login_required(login_url = '/login/')

def show_specific_report(request, id):
    if not request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    report_objects = Report.objects.filter(admin_submission = request.user, id=id)
    return HttpResponse(
        serializers.serialize('json', report_objects),
        report_objects,
        )
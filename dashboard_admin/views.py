from django.shortcuts import render, redirect
from dashboard_admin.forms import FeedbackForm
from submission_form.models import Report
from dashboard_admin.models import Feedback
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
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

# FORM

@login_required(login_url='/login/')
def show_reminder_form(request):
    context = {}
    if not request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    notes_objects = Feedback.objects.all()
    context = {
        "notes_objects": notes_objects,
        "username": request.user,
    }
    return render(request, 'admin_rem.html', context)

@login_required(login_url='/login/')
def get_reminder_json(request):
    data = Feedback.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/login/')
def create_note(request):
    if request.POST:
        form = FeedbackForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            form = FeedbackForm()
            pesan = "Catatan berhasil dibuat"
            messages.success(request, 'Catatan telah berhasil dibuat!')
            context = {
                "form": form,
                "pesan": pesan,
            }
            return HttpResponse(
                serializers.serialize("json", [new_form]),
                content_type="application/json",
            )
        else:
            print(100)
            messages.error(
                request, 'Lengkapi catatan Admin!')
            form = FeedbackForm()
            context = {
                "form": form,
            }

    else:
        form = FeedbackForm()
        context = {
            "form": form,
        }
    return render(request, "admin_rem.html", context)


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
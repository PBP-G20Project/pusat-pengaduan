from django.shortcuts import render, redirect
# from submission_form.models import Report
from django.http import HttpResponse
from django.core import serializers
from submission_form.models import Report
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/login/')
def show_reports(request):
    if request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    return render(request,"user-dashboard.html")

@login_required(login_url='/login/')
def get_all_reports(request):
    if request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    data = Report.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url = '/login/')
def get_unprocessed_reports(request):
    if request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    data = Report.objects.filter(user=request.user, status ="Belum")
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url = '/login/')
def get_onprogress_reports(request):
    if request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    data = Report.objects.filter(user = request.user ,status ='Sedang')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url = '/login/')
def get_processed_reports(request):
    if request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    data = Report.objects.filter(user=request.user, status='Sudah')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
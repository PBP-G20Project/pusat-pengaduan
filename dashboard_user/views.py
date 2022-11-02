from django.shortcuts import render, redirect
# from submission_form.models import Report
from django.http import HttpResponse
from django.core import serializers
from submission_form.models import Report
from dashboard_user.models import Draft
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url = '/login/')
def show_reports(request):
    if request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    context = {
        "report": Report.objects.filter(user_submission = request.user),
        "username": request.user,
    }
    return render(request,"user-dashboard.html",context)

@login_required(login_url='/login/')
def get_all_reports(request):
    if request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    data = Report.objects.filter(user_submission = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url = '/login/')
def get_unprocessed_reports(request):
    if request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    data = Report.objects.filter(user_submission=request.user, status ="PENDING")
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url = '/login/')
def get_onprogress_reports(request):
    if request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    data = Report.objects.filter(user_submission = request.user ,status ='DIPROSES')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url = '/login/')
def get_processed_reports(request):
    if request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    data = Report.objects.filter(user_submission =request.user, status='SELESAI')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url = '/login/')
def get_rejected_reports(request):
    data = Report.objects.filter(user_submission=request.user, status='REJECTED')
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url = '/login/')
@csrf_exempt
def add_draft(request):
    context = {}
    if request.method == "POST":
        temp = Draft(user=request.user, title=request.POST.get('title'), description=request.POST.get('description'))
        temp.save()
        return JsonResponse({'message': 'success'})

@login_required(login_url = '/login/')
def show_draft_json(request):
    data = Draft.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
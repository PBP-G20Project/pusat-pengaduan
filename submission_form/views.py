import json
from submission_form.forms import ReportForm
from submission_form.models import Report
from login_things.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import random
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def show_form(request):
    if request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    if not request.user.is_authenticated:
        nama = "belum login"
    else:
        nama = request.user.nama
    context = {'nama':nama}
    return render(request, 'form.html', context)

@login_required(login_url='/login/')
def get_json(request):
    data = Report.objects.filter(user_submission=request.user) # filter by user
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@login_required(login_url='/login/')
def create_report(request):
    if request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    data_admin = User.objects.filter(admin=True).filter(staff=False)
    if len(data_admin) != 0:
        index = random.randint(0, len(data_admin)-1)
    elif len(data_admin) == 0:
        index = -1

    # Logic Assign Admin
    # admin_assign = None
    # if len(data_admin) != 0:
    #     admin_assign = data_admin[0]
    #     for admin in data_admin:
    #         if admin.counter < admin_assign.counter:
    #             admin_assign = admin

    # print(data_admin[0])
    if request.method == 'POST':
        # print(request.method)
        # create a form instance and populate it with data from the request:
        form = ReportForm(request.POST)
        
        if index == -1:
            dataAdmin = None
        else:
            dataAdmin = data_admin[index]
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            report = Report(
                user_submission = request.user,
                # admin_submission = admin_assign,
                admin_submission = dataAdmin,
                title = form.cleaned_data['title'],
                content = form.cleaned_data['content'],
                institution = form.cleaned_data['institution'],
                institution_level = form.cleaned_data['institution_level'],
                involved_party = form.cleaned_data['involved_party'],
                location = form.cleaned_data['location'],
                date = form.cleaned_data['date'],
                status = "PENDING"
            )
            # admin_assign.counter += 1
            report.save()
            # redirect to a new URL:
            print("success")
            return HttpResponse(
                serializers.serialize("json", [report]),
                content_type="application/json",
            )


    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReportForm()

    return render(request, 'form.html', {'form': form})

@csrf_exempt
def add_report_flutter(request):
    data_admin = User.objects.filter(admin=True).filter(staff=False)
    if len(data_admin) != 0:
        index = random.randint(0, len(data_admin)-1)
    elif len(data_admin) == 0:
        index = -1

    if request.method == 'POST':
        if index == -1:
            dataAdmin = None
        else:
            dataAdmin = data_admin[index]

        data = json.loads(request.body)
    
        report = Report(
            user_submission = request.user,
            admin_submission = dataAdmin,
            title = data['title'],
            content = data['content'],
            institution = data['institution'],
            institution_level = data['institution_level'],
            involved_party = data['involved_party'],
            location = data['location'],
            date = data['date'],
            status = "PENDING"
        )
        report.save()
        return JsonResponse({"status": "success"}, status = 200)
    else:
        return JsonResponse({"status": "error"}, status = 401)
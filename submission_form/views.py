from submission_form.forms import ReportForm
from submission_form.models import Report
from login_things.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import random
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def show_form(request):
    context = {}
    return render(request, 'form.html', context)

@login_required(login_url='/login/')
def get_json(request):
    data = Report.objects.all() # filter by user
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@login_required(login_url='/login/')
def create_report(request):
    data_admin = User.objects.filter(admin=True).filter(staff=False)
    index = random.randint(0, len(data_admin)-1)
    # dapatkan index admin dengan counter terendah

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
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            report = Report(
                user_submission = request.user,
                # admin_submission = admin_assign,
                admin_submission = data_admin[index],
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

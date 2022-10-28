from submission_form.forms import ReportForm
from submission_form.models import Report
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.core import serializers

# Create your views here.
@csrf_exempt
def show_form(request):
    context = {}
    return render(request, 'form.html', context)

def get_json(request):
    data = Report.objects.all() # filter by user
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def create_report(request: HttpRequest):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReportForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            report = Report(
                user = "user1",
                title = form.cleaned_data['title'],
                content = form.cleaned_data['content'],
                date = form.cleaned_data['date'],
                location = form.cleaned_data['location'],
                institution = form.cleaned_data['institution'],
                involved_party = form.cleaned_data['involved_party'],
                status = "PENDING"
            )
            report.save()
            messages.success(request, 'Laporan berhasil dibuat')
            # redirect to a new URL:
            print("success")
            return HttpResponse(
                serializers.serialize("json", [report]),
                content_type="application/json",
            )
        else:
            print("error")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReportForm()
        print("error2")

    return render(request, 'form.html', {'form': form})

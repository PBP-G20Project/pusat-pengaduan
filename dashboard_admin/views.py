from django.shortcuts import render, redirect
#from submission_form.models import Report
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
#@login_required(login_url = '/login_things/')
def show_laporan(request):
    context = {
        "username": request.user}
    return render(request, "accusation.html", context)
'''
@login_required(login_url = "/login_things/")
def update_laporan_1 (request, id):
    laporan = Report.objects.get(user = request.user, id=id)
    laporan.dieksekusi = not (laporan.dieksekusi)
    laporan.save(update_fields = ["dieksekusi"])
    return HttpResponseRedirect(reverse("dashboard_admin:show_laporan"))

@login_required(login_url = "/login_things/")
def update_laporan_2 (request, id):
    laporan = Report.objects.get(user = request.user, id=id)
    laporan.selesai = not (laporan.selesai)
    laporan.save(update_fields = ["selesai"])
    return HttpResponseRedirect(reverse("dashboard_admin:show_laporan"))
'''
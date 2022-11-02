from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from login_things.forms import SignUpForm, EditForm
from login_things.models import User
from django.core import serializers
import datetime
import time
from django.contrib.auth.decorators import login_required


# Create your views here.
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun telah berhasil dibuat!")
            return redirect('login:login_user')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def register_user_admin(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            registrasi = form.save(commit=False)
            registrasi.admin = True
            registrasi.save()
            messages.success(request, "Akun telah berhasil dibuat!")
            return redirect('login:login_user')
    context = {
        'form': form
    }
    return render(request, 'register_admin.html', context)


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(
                reverse("main_page:show_main_page"))  # membuat response
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Email atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# dummy testing
def dummy(request):
    context = {
        'nama': request.user.nama,
        'is_staff': request.user.staff,
        'is_admin': request.user.admin,
        # 'last_login': request.COOKIES['last_login'],

    }
    return render(request, "dummy.html", context)


@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('login:login_user'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login/')
def show_profile(request, id):
    if request.user.id != id:
        return redirect("login:error_page")
    user_data = User.objects.get(id=id)
    form = EditForm(request.POST, instance=user_data)
    already_show = False
    if request.method == "POST":
        if form.is_valid():
            user_data.nama = form.cleaned_data['nama']
            user_data.email = form.cleaned_data['email']
            user_data.nik = form.cleaned_data['nik']
            user_data.save()
            return HttpResponse(
                serializers.serialize("json", [user_data]),
                content_type="application/json",
            )    
    else:
        already_show = True
    context = {
        "user" : user_data,
        "form" : form,
        "already_show" : already_show
    }
    return render(request, "profile.html", context)

@login_required(login_url='/login/')
def get_json(request):
    data = User.objects.all() # filter by user
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def error_page(request):
    return render(request, "error_page.html")

@login_required(login_url='/login/')
def get_dashboard(request):
    if request.user.admin:
        return redirect('dashboard_admin:show_report')
    else:
        return redirect('dashboard_user:show_reports')


from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from login_things.forms import SignUpForm
import datetime


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
                reverse("login:dummy"))  # membuat response
            # membuat cookie last_login dan menambahkannya ke dalam response
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Email atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# dummy testing


def dummy(request):
    context = {
        'nama': request.user.nama,
        'is_staff': request.user.staff,
        'is_admin': request.user.admin,
        'last_login': request.COOKIES['last_login'],

    }
    return render(request, "dummy.html", context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('login:login_user'))
    response.delete_cookie('last_login')
    return response

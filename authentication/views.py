from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from login_things.models import User
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from login_things.forms import SignUpForm, EditForm

@csrf_exempt
def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(username=email, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "message": "Successfully Logged In!"
              # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Login, Account Disabled."
            }, status=401)
    else:
        return JsonResponse({
          "status": False,
          "message": "Failed to Login, check your email/password."
        }, status=401)

# @login_required(login_url='/login/')
def data_login(request):
  if(str(request.user) == "AnonymousUser"):
    return JsonResponse({
          "status": False,
          "message": "Belum login"
        }, status=401)
  user_data = User.objects.filter(id=request.user.id)
  return HttpResponse(serializers.serialize('json', user_data), content_type="application/json")

@csrf_exempt
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
              "status": True,
              "message": "Akun ditambahkan"
              # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
          return JsonResponse({
          "status": False,
          "message": "Data yang diberikan tidak valid"
        }, status=401)
    
    return JsonResponse({
          "status": False,
          "message": "Tidak ada data yang diberikan"
        }, status=401)


@csrf_exempt
def profile(request):
    if(str(request.user) == "AnonymousUser"):
      return JsonResponse({
            "status": False,
            "message": "Belum login"
          }, status=401)
    user_data = User.objects.get(id=request.user.id)
    form = EditForm(request.POST, instance=user_data)
    print(request.POST, user_data)
    if request.method == "POST":
        if form.is_valid():
            user_data.nama = form.cleaned_data['nama']
            user_data.email = form.cleaned_data['email']
            user_data.nik = form.cleaned_data['nik']
            user_data.save()
            return JsonResponse({
              "status": True,
              "message": "Berhasil Ubah Data"
            }, status=401)
        else:
          return JsonResponse({
          "status": False,
          "message": "Data yang diberikan tidak valid"
        }, status=401)
    
    return JsonResponse({
          "status": False,
          "message": "Tidak ada data yang diberikan"
        }, status=401)

from urllib import request
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from login_things.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import *
from django.core import serializers
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def show_main_page(request):
    if not request.user.is_authenticated:
        nama = "belum login"
    else:
        nama = request.user.nama
    review_data = Reviews.objects.all()
    full_name_list = []
    for i in range(len(review_data)):
        temp = User.objects.filter(id=review_data[i].user.id)
        full_name_list.append(temp[0].nama)
    len_list = len(full_name_list)
    review_data = zip(review_data, full_name_list)
    konteks = {
        "review_data": review_data,
        "full_name_list": full_name_list,
        "len_list": len_list,
        "nama": nama
    }
    return render(request, "main_page.html", konteks)


@login_required(login_url='/login/')
@csrf_exempt
def create_review(request):
    print(request.user.admin)
    if request.user.admin and not request.user.staff:
        return redirect("login:error_page")
    if request.POST:
        form = FormReviews(request.POST)
        print(request.POST)
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.user = request.user
            task_list.save()
            form = FormReviews()
            pesan = "Review berhasil dibuat"
            messages.success(request, 'Review telah berhasil dibuat!')
            konteks = {
                "form": form,
                "pesan": pesan,
            }
            return JsonResponse({
                "status": True,
                "message": "Berhasil buat Review"
            }, status=401)
        else:
            return JsonResponse({
                "status": False,
                "message": "Gagal buat Review, Cek Kembali"
            }, status=401)

# def show_news_1(request) :
#     form = PostForms(request.POST)
#     if request.method == 'POST' :
#         if form.is_valid() :
#             form.save()
#             return HttpResponseRedirect(reverse("main_page:show_news_1"))

#     context = {'form' : form}
#     return render(request, 'news_1.html', context)


def show_news_1(request):
    return render(request, "news_1.html")


def show_news_2(request):
    return render(request, "news_2.html")


def show_news_3(request):
    return render(request, "news_3.html")


@login_required(login_url='/login/')
def get_json(request):
    data = Reviews.objects.all()  # filter by user
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


# def show_news_2(request) :
#     form = PostForms(request.POST)
#     if request.method == 'POST' :
#         if form.is_valid() :
#             form.save()
#             return HttpResponseRedirect(reverse("main_page:show_news_2"))

#     context = {'form' : form}
#     return render(request, 'news_2.html', context)

# def show_news_3(request) :
#     form = PostForms(request.POST)
#     if request.method == 'POST' :
#         if form.is_valid() :
#             form.save()
#             return HttpResponseRedirect(reverse("main_page:show_news_3"))

#     context = {'form' : form}
    # return render(request, 'news_3.html', context)


def show_json(request):
    task = Reviews.objects.all()
    return HttpResponse(serializers.serialize('json', task), content_type='application/json')

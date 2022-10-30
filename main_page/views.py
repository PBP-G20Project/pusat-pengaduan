from urllib import request
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *
from django.core import serializers
from django.urls import reverse


# Create your views here.
def show_main_page(request):
    review_data = Reviews.objects.all()
    konteks = {
        "review_data": review_data
    }
    return render(request, "main_page.html", konteks)


def create_review(request):
    if request.POST:
        form = FormReviews(request.POST)
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.user = request.user
            task_list.save()
            form = FormReviews()
            pesan = "Data berhasil disimpan"
            konteks = {
                "form": form,
                "pesan": pesan,
            }
            render(request, "create_review.html", konteks)
        else:
            messages.error(request, 'Rating harus berada pada rentang 1 sampai 5')
            form = FormReviews()
            konteks = {
                "form": form,
            }

    else:
        form = FormReviews()
        konteks = {
            "form": form,
        }
    return render(request, "create_review.html", konteks)

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

# def show_json(request):
#     task = Comments.objects.all()
#     return HttpResponse(serializers.serialize('json', task), content_type='application/json')

from urllib import request
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .models import Comments
from .forms import *
from django.core import serializers
from django.urls import reverse


# Create your views here.
def show_main_page(request) :
    return render (request, "main_page.html")

# def show_news_1(request) :
#     form = PostForms(request.POST)
#     if request.method == 'POST' :
#         if form.is_valid() :
#             form.save()
#             return HttpResponseRedirect(reverse("main_page:show_news_1"))

#     context = {'form' : form}
#     return render(request, 'news_1.html', context)

def show_news_1(request) :
    return render(request,"news_1.html")

def show_news_2(request) :
    return render(request,"news_2.html")

def show_news_3(request) :
    return render(request,"news_3.html")

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
    return render(request, 'news_3.html', context)

def show_json(request):
    task = Comments.objects.all()
    return HttpResponse(serializers.serialize('json', task), content_type='application/json')
            
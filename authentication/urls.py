from django.contrib import admin
from django.urls import path
from authentication.views import *

app_name = 'login_baru'

urlpatterns = [
    path('login/', login, name='login'),
    path('data_login/', data_login, name='data_login'),
]
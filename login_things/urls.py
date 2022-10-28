from django.contrib import admin
from django.urls import path
from login_things.views import login_user, register_user, dummy, logout_user, register_user_admin

app_name = 'login'

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('register/', register_user, name='register_user'),
    path('register_admin/', register_user_admin, name='register_admin'),
    path('dummy/', dummy, name='dummy'),
    path('logout/', logout_user, name='logout'),

]
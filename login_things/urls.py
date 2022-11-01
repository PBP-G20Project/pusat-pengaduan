from django.contrib import admin
from django.urls import path
from login_things.views import *

app_name = 'login'

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('register/', register_user, name='register_user'),
    path('register_admin/', register_user_admin, name='register_admin'),
    path('dummy/', dummy, name='dummy'),
    path('logout/', logout_user, name='logout'),
    path('profile/<int:id>', show_profile, name='show_profile'),

]
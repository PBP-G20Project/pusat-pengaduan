from django.urls import path
from submission_form.views import show_form, get_json, create_report

app_name = 'submission_form'
urlpatterns = [
    path('', show_form, name='submission_form'),
    path('json/', get_json, name='get_json'),
    path('create/', create_report, name='create_report'),
]
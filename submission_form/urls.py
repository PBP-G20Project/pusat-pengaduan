from django.urls import path
from submission_form.views import add_report_flutter, show_form, get_json, create_report

app_name = 'submission_form'
urlpatterns = [
    path('', show_form, name='submission_form'),
    path('json/', get_json, name='get_json'),
    path('create/', create_report, name='create_report'),
    path('add_report_flutter/', add_report_flutter, name='add_from_flutter')
]
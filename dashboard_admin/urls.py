from django.urls import path
from dashboard_admin.views import create_note
from dashboard_admin.views import show_report
from dashboard_admin.views import report_next
from dashboard_admin.views import report_prev
from dashboard_admin.views import report_reject
from dashboard_admin.views import show_specific_report
from dashboard_admin.views import show_all_report
from dashboard_admin.views import show_all_pending
from dashboard_admin.views import show_all_diproses
from dashboard_admin.views import show_all_selesai
from dashboard_admin.views import show_all_ditolak
from dashboard_admin.views import show_reminder_form
from dashboard_admin.views import get_reminder_json
from dashboard_admin.views import add_reminder_json
from dashboard_admin.views import create_reminder

app_name = 'dashboard_admin'

urlpatterns = [
    path('', show_report, name='show_report'),
    path('report_next/<int:id>/', report_next, name='report_next'),
    path('report_prev/<int:id>/', report_prev, name='report_prev'),
    path('report_reject/<int:id>/', report_reject, name='report_reject'),
    path('show_reminder_form/', show_reminder_form, name='show_reminder_form'),
    path('create_note/', create_note, name='create_note'),
    path('create_reminder/', create_reminder, name='create_reminder'),
    path('add_reminder_json/', add_reminder_json, name='add_reminder_json'),
    path('get_reminder_json/', get_reminder_json, name='get_reminder_json'),
    path('show_all_report/', show_all_report, name='show_all_report'),
    path('show_all_pending/', show_all_pending, name='show_all_pending'),
    path('show_all_diproses/', show_all_diproses, name='show_all_diproses'),
    path('show_all_selesai/', show_all_selesai, name='show_all_selesai'),
    path('show_all_ditolak/', show_all_ditolak, name='show_all_ditolak'),
    path('show_specific_report/<int:id>/', show_specific_report, name='show_specific_report'),
]
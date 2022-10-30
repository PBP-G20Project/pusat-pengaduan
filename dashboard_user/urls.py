from django.urls import path
from dashboard_user.views import *

app_name = 'dashboard_user'

urlpatterns = [
    path('', show_reports, name='show_reports'),
    path('Laporan/', get_all_reports, name = 'get_all_reports'),
    path('BelumDitangani/', get_onprogress_reports, name='get_onprogress_reports'),
    path('SedangDitangani/',get_processed_reports, name = 'get_processed_reports'),
    path('SudahDitanangi/', get_unprocessed_reports, name = 'get_unprocessed_reports')
]
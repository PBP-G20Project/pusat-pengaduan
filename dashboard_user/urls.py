from django.urls import path
from dashboard_user.views import *

app_name = 'dashboard_user'

urlpatterns = [
    path('', show_reports, name='show_reports'),
    path('Laporan/', get_all_reports, name = 'get_all_reports'),
    path('SedangDitangani/', get_onprogress_reports, name='get_onprogress_reports'),
    path('SudahDitangani/',get_processed_reports, name = 'get_processed_reports'),
    path('BelumDitangani/', get_unprocessed_reports, name = 'get_unprocessed_reports'),
    path('Draft/', add_draft, name = 'add_draft'),
    path('ShowDraft/', show_draft_json, name = 'show_draft_json')
]
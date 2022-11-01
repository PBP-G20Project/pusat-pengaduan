from django.urls import path
from dashboard_admin.views import show_report
# from dashboard_admin.views import update_diproses
# from dashboard_admin.views import update_selesai

app_name = 'dashboard-admin'

urlpatterns = [
    path('', show_report, name='show_report'),
]
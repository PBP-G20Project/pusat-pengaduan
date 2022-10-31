from django.urls import path
from dashboard_admin.views import show_report
from dashboard_admin.views import update_diproses
from dashboard_admin.views import update_selesai

app_name = 'dashboard-admin'

urlpatterns = [
    path('', show_report, name='show_report'),
    path('update_diproses/<int:id>/', update_diproses, name='update_diproses'),
    path('update_selesai/<int:id>/', update_selesai, name='update_selesai'),
]
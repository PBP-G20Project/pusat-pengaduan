from django.urls import path
from dashboard_admin.views import show_report
from dashboard_admin.views import report_next
from dashboard_admin.views import report_prev
from dashboard_admin.views import report_reject

app_name = 'dashboard_admin'

urlpatterns = [
    path('', show_report, name='show_report'),
    path('report_next/<int:id>/', report_next, name='report_next'),
    path('report_prev/<int:id>/', report_prev, name='report_prev'),
    path('report_reject/<int:id>/', report_reject, name='report_reject'),
]
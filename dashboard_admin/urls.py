from django.urls import path
from dashboard_admin.views import show_laporan
#from dashboard_admin.views import update_laporan_1
#from dashboard_admin.views import update_laporan_2

app_name = 'dashboard-admin'

urlpatterns = [
    path('', show_laporan, name='show_laporan'),
    #path('update_laporan_1/<int:id>/', update_laporan_1, name='update_status_laporan'),
    #path('update_laporan_2/<int:id>/', update_laporan_2, name='update_status_laporan'),
]
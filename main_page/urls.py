from django.urls import path
from main_page.views import *

app_name = 'main_page'

urlpatterns = [
    path('', show_main_page, name='show_main_page'),
    path('news_1/', show_news_1, name='show_news_1'),
    path('news_2/', show_news_2, name='show_news_2'),
    path('news_3/', show_news_3, name='show_news_3'),
    path('isi_form/', create_review, name='create_review'),
    path('json_review/', get_json, name='get_json'),
    path('json_name/', get_json_name, name='get_json_name'),

]

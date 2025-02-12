from django.urls import path
from .views import file_list, download_file



urlpatterns =[
    path('', file_list, name='file_list'),
    path('download/<int:file_id>/', download_file, name='download_file'),
]


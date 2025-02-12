from django.urls import path
from .views import file_list, download_file
from django.conf.urls.static import static
from django.conf import settings


urlpatterns =[
    path('', file_list, name='file_list'),
    path('download/<int:file_id>/', download_file, name='download_file'),
]

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
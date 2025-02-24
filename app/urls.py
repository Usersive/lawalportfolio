from django.conf import settings
from django.urls import path
from .views import  download_file
from django.conf.urls.static import static

urlpatterns =[
    # path('download/<int:file_id>/', download_file, name='download_file'),
    path('download/<str:file_id>/', download_file, name='download_file'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
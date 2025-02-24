"""myportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from .views import index, download_file, subscribe_newsletter, unsubscribe, favicon_view



urlpatterns = [
    path('horenadmin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('portfolioadmin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('', views.index, name="index"),
    
    path('email_compose/', views.email_compose, name='email_compose'),
    
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('download/', download_file, name='download_file'),  
    path('subscribe/', subscribe_newsletter, name='subscribe_newsletter'),
    path("unsubscribe/<uuid:token>/", unsubscribe, name="unsubscribe"),
    
    path('favicon.ico', favicon_view, name="favicon"),
    
    path('download/<str:file_id>/', download_file, name='download_file'),
    
]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
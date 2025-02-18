"""
Django settings for myportfolio project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
import dj_database_url
import environ
import cloudinary
import cloudinary.uploader
import cloudinary.api
from decouple import config
from cloudinary.utils import cloudinary_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY =('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = True
DEBUG = os.environ.get('DEBUG', 'True')=="True"


ALLOWED_HOSTS = ['127.0.0.1', 'lawalportfolio.onrender.com']

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'cloudinary_storage',
    'cloudinary',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myportfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'myportfolio.date.current_year',
            ],
        },
    },
]

WSGI_APPLICATION = 'myportfolio.wsgi.application'
CSRF_COOKIE_SECURE = True  # Ensures CSRF cookie is only sent over HTTPS

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'), 
        'USER': config('USER'),  
        'PASSWORD': config('PASSWORD'),  
        'HOST': config('HOST'),  
        'PORT': config('PORT', "8000"),  
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Lagos' 

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



from django.contrib.messages import constants as messages
MESSAGE_TAGS ={
    messages.ERROR: 'danger',
}





STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
        }
}

#CLOUDINARY SETUP 
CLOUDINARY_URL = config('CLOUDINARY_URL') 

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUD_NAME'),
    'API_KEY': config('API_KEY'),
    'API_SECRET': config('API_SECRET'),
}

# CLOUDINARY SETUP FOR MEDIA
DEFAULT_FILE_STORAGE ='cloudinary_storage.storage.RawMediaCloudinaryStorage'

# #Load barcode user image from cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


EMAIL_BACKEND       = config('EMAIL_BACKEND')   
EMAIL_HOST          = config('EMAIL_HOST')  
EMAIL_PORT          = config('EMAIL_PORT', cast=int) 
EMAIL_HOST_USER     = config('EMAIL_HOST_USER')    
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')    
EMAIL_USE_TLS       = config('EMAIL_USE_TLS', cast=bool)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Security settings for production
SECURE_SSL_REDIRECT = True  # Redirects all HTTP requests to HTTPS
SESSION_COOKIE_SECURE = True  # Ensures session cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True  # Ensures CSRF cookie is only sent over HTTPS
X_FRAME_OPTIONS = 'DENY'  # Prevents your site from being loaded in an iframe (Clickjacking protection)
SECURE_HSTS_SECONDS = 31536000  # Enforces HTTPS for 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


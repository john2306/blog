from .base import *

DEBUG = False
ALLOWED_HOSTS = ['johnmendoza.tk','www.johnmendoza.tk','161.35.61.141','*.johnmendoza.tk']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dreamdb',
        'USER': 'dream_admin',
        'PASSWORD': 'qazwsx,.-UNI',
        'HOST': 'localhost',
        'PORT': '',
    }
}
STATICFILES_DIRS = (BASE_DIR, 'static')
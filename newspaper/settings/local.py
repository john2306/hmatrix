from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1:8080', '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')
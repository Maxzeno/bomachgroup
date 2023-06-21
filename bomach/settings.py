"""
Django settings for bomach project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(config('DEBUG', 0)))

# use local db, storage, email config create be me
TRY_LOCAL_DB = bool(int(config('TRY_LOCAL_DB', 0)))
TRY_LOCAL_STORAGE = bool(int(config('TRY_LOCAL_STORAGE', 0)))
TRY_LOCAL_EMAIL = bool(int(config('TRY_LOCAL_EMAIL', 0)))

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

_ALLOWED_HOST = config('ALLOWED_HOST')
if _ALLOWED_HOST:
    ALLOWED_HOSTS.extend(_ALLOWED_HOST.split())

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'main',
]

if not TRY_LOCAL_STORAGE:
    INSTALLED_APPS.append('cloudinary')
    INSTALLED_APPS.append('cloudinary_storage')

    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': config('CLOUDINARY_STORAGE_CLOUD_NAME'),
        'API_KEY': config('CLOUDINARY_STORAGE_API_KEY'),
        'API_SECRET': config('CLOUDINARY_STORAGE_API_SECRET')
    }


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'bomach.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bomach.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if TRY_LOCAL_DB:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3-test',
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': config('DATABASES_DEFAULT_ENGINE'),
            'NAME': config('DATABASES_DEFAULT_NAME'),
            'HOST': config('DATABASES_DEFAULT_HOST'),
            'PORT': int(config('DATABASES_DEFAULT_PORT')),
            'USER': config('DATABASES_DEFAULT_USER'),
            'PASSWORD': config('DATABASES_DEFAULT_PASSWORD'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
   BASE_DIR / 'static'
]

MEDIA_URL = '/media/'    

MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

###DEVELOPMENT

if TRY_LOCAL_EMAIL:
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = '1025'

###PRODUCTION

else:
    EMAIL_HOST = config('EMAIL_HOST', 'smtp.gmail.com')
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    EMAIL_PORT = config('EMAIL_PORT', '587')
    EMAIL_USE_TLS = bool(config('EMAIL_USE_TLS', True))


CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'width': '100%',
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Strike'],
            ['NumberedList', 'BulletedList', 'Outdent', 'Indent'],
            ['Link', 'Unlink', 'Anchor'],
            ['Undo', 'Redo'],
            ['Format', 'Styles'],
            ['RemoveFormat', 'Source']
        ],
        'removePlugins': 'image',
        # 'removeButtons': 'Source',
    }
} 

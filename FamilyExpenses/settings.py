import os.path
from os.path import abspath, basename, dirname, join, normpath
from sys import path

from pathlib import Path

from django.contrib import messages
from django.urls import reverse_lazy
import environ

BASE_DIR = dirname(dirname(__file__) + "../../../")

CONFIG_ROOT = dirname(dirname(abspath(__file__)))
PROJECT_ROOT = dirname(CONFIG_ROOT)

env = environ.Env()
env.read_env(env_file=join(PROJECT_ROOT, ".env"))
SECRET_KEY = 'django-insecure-_w7$ih&fr7xpkfm!qh7ka4@joc_b#9!%56x5%^)-yg%mylhg#!'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'crispy_forms',
    'django_extensions',
    'rest_framework',

    'expense',
    'accounts',
    'userperferences',
    'income',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FamilyExpenses.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [BASE_DIR, normpath(join(PROJECT_ROOT, "templates"))],
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

WSGI_APPLICATION = 'FamilyExpenses.wsgi.application'

AUTH_USER_MODEL = 'accounts.User'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.str("DB_NAME", ""),
        'USER': env.str("DB_USER", ""),
        'PASSWORD': env.str("DB_USER_PASSWORD", ""),
        'HOST': env.str("DB_HOST", ""),
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'FamilyExpenses/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = [BASE_DIR, normpath(join(PROJECT_ROOT, "templates"))]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SMTP_ENABLED = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'expenseq@gmail.com'
EMAIL_HOST_PASSWORD = 'dwkscokpbzcrmzkq'

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

LOGIN_REDIRECT_URL = reverse_lazy('expenses-dash:expenses')

from pathlib import Path

import os
import django_heroku
import dj_database_url
from dotenv import load_dotenv
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'blogTi.apps.BlogtiConfig',
    'contato.apps.ContatoConfig',
    'autenticacao.apps.AutenticacaoConfig',
    'cursos.apps.CursosConfig',
    'contas.apps.ContasConfig',
    'quiz.apps.QuizConfig',
    'ckeditor',
    'ckeditor_uploader',
    'widget_tweaks',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

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
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'blog.wsgi.application'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
   'default': {
   'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'dc28e69v6fdemu',
          'USER': 'ejgsnubywnehpw',
          'PASSWORD': '825163156b52a8973126bfc208fe561022db2fe62cb2e54ba4fa521b48186a1d',
          'HOST': 'ec2-3-232-62-229.compute-1.amazonaws.com',
          'PORT': '5432',
          'OPTIONS': {
                    'options': '-c search_path=public'
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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

#STATIC_URL = 'static/'
#STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL)

#MEDIA_URL = '/image/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

#storage google

from google.oauth2 import service_account
GS_CREDENTIALS = service_account.Credentials.from_service_account_file(os.path.join(BASE_DIR, 'credential.json'))

DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_PROJECT_ID = 'blog'
GS_BUCKET_NAME = 'blogbe_bucket'
MEDIA_ROOT = 'media/'
UPLOAD_ROOT = 'media/uploads/'
MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_BUCKET_NAME)
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'


CKEDITOR_UPLOAD_PATH = 'uploads/'
STATIC_ROOT = os.path.join(BASE_DIR,  'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
#STATICFILES_DIRS = [
 #   os.path.join(BASE_DIR, 'staticfiles/')
#]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




#google config
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'default from email'

SITE_ID = 1

django_heroku.settings(locals())

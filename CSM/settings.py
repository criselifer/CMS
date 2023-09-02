"""
Django settings for CSM project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-x035hw9rb)r_^e6hwa-e=1ygc%&n(-oll8#qspc@w$mlkd9dw-"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'home',
    'contenido',

    "crispy_forms",
    "crispy_bootstrap5",

]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "CSM.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = "CSM.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
	"USER": "postgres",
	"PASSWORD": "postgres",
	"HOST": "db",
	"PORT": "5433",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "es-py"

TIME_ZONE = "America/Asuncion"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# configuraciones adicionales del sso

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
#EMAIL_BACKEND = [Mi configuracion de correo]

# Configuracion de django-allout, que sirve para redireccionar al home una vez iniciado sesion
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS =True
LOGIN_REDIRECT_URL = 'home'

# Configuracion de django-allout, que sirve para iniciar con el user o con el correo
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

# Configuracion de django-allout, que sirve para que el correo sea requerido al registrarse
ACCOUNT_EMAIL_REQUIRED = True

# Configuracion de django-allout, que sirve para que solamente se pueda crear un usuario por correo
ACCOUNT_UNIQUE_EMAIL = True

# Configuracion de django-allout. Indica que al crearse una nueva cuenta, el usuario primero deba verificar su correo antes de poner iniciar sesion
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Configuracion de django-allout. Indica que pasado 7 dias luego de haber mandado el correo de confimarcion, este expira
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7

# Configuracion de django-allout. Al darle a cerrar sesion, este se deslogea automaticamente sin preguntar
# ACCOUNT_LOGOUT_ON_GET = True

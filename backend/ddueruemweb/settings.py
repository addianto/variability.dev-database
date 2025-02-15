"""
Django settings for ddueruemweb project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import logging
import os
import dotenv

from pathlib import Path

# env = environ.Env(DEBUG=(bool, False))
# environ.Env.read_env()

dotenv.load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', "****")
print("AAAAAAAAA",SECRET_KEY)
if not SECRET_KEY:
    SECRET_KEY = "****"
print("AAAAAAAAA",SECRET_KEY)

# SECRET_KEY = env()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', True)

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'core',
    'core.user',
    'core.fileupload',
    'core.analysis',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_filters',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_seed',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'ddueruemweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': os.getenv('TEMPLATE_DEBUG', True),
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ddueruemweb.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {}

if os.getenv('USE_POSTGRES', False) != 'True':
    DATABASES = {
        # Should be in the environment as well
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('DB_NAME','ddueruem'),
            'USER': os.getenv('DB_USER','ddueruem'),
            'PASSWORD': os.getenv('DB_PASSWORD','***'),
            'HOST': os.getenv('DB_HOST','ddueruem'),
            'PORT': os.getenv('DB_PORT','5432'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    #    {
    #        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    #    },
    #    {
    #        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #    },
    #    {
    #        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #    },
    #    {
    #        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    #    },
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        # enable django rest framework rendering in browser
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'core_user.User'

# LOGIN_REDIRECT_URL = "dashboard"  # define URL to which user should be redirected after successful login
# LOGOUT_REDIRECT_URL = "home"
ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

# https://docs.djangoproject.com/en/3.2/topics/email/
EMAIL_HOST = os.getenv('EMAIL_HOST','mail')  # define host and port for email backend
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER','mail')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD','***')
EMAIL_PORT = os.getenv('EMAIL_PORT','2525')
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False

# also used for user email activation (token) timeout and file confirmed time calculation
PASSWORD_RESET_TIMEOUT_DAYS = 2
# Customize Logging details: https://docs.djangoproject.com/en/4.0/howto/logging/
if DEBUG:
    # only print logger.debug(...) to console if DEBUG is active
    # also includes logger.info(...)
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s',
    )
LOGGING = {
    'version': 1,  # the dictConfig format version
    'disable_existing_loggers': False,  # retain the default loggers
}

SECURE_SSL_REDIRECT = os.getenv("USE_SSL",False) == True
SECURE_PROXY_SSL_HEADER = None

if os.getenv("USE_SSL", False):
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURE_SSL_REDIRECT = False
# SECURE_PROXY_SSL_HEADER = None

# if False:
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

GITHUB_AUTH = True

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "none"
REST_USE_JWT = True


if GITHUB_AUTH:
    AUTHENTICATION_BACKENDS = (
        'allauth.account.auth_backends.AuthenticationBackend',
        'django.contrib.auth.backends.ModelBackend',
    )
    SOCIALACCOUNT_PROVIDERS = {
        'github': {
            'SCOPE': [
                'user:email',
            ],
        }
    }

    SOCIALACCOUNT_ADAPTER = 'core.adapter.AccountAPIAdapter'

    GITHUB_AUTH_CALLBACK = "https://ddueruem.tobiasbetz.de/github_confirm"

    #GITHUB_AUTH_CALLBACK = "https://google.com"

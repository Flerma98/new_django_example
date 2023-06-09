import json
import os
from pathlib import Path

from django.core.checks import templates
from django.template.context_processors import media


def load_settings():
    config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config.json')
    with open(config_file_path) as config_file:
        return json.load(config_file)


config = load_settings()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-426#-^mq7hm+8!1rxe6a&h471rra*07*^z4l0j@#eod@lla8sr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition
CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'corsheaders'
]

LIBRARY_APPS = [
    'knox',
    'drf_query_filter',
    'django_cleanup'
]

PROJECT_APPS = [
    'apps.restaurants',
    'apps.foods',
    'apps.users',
    'apps.users.user_profile',
    'apps.auth_users'
]

INSTALLED_APPS = CORE_APPS + LIBRARY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'knox.auth.TokenAuthentication',
        'django_example.bearer_override.BearerTokenAuthentication'
    ],
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer', ],
    'DEFAULT_PARSER_CLASSES': ['rest_framework.parsers.JSONParser', ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'lib.pagination.SearchPagination',
    'DEFAULT_FILTER_BACKENDS': (
        'drf_query_filter.filters.QueryParamFilter',
    )
}

CORS_ORIGIN_ALLOW_ALL = True

REST_KNOX = {
    'AUTH_HEADER_PREFIX': 'bearer',
    'TOKEN_TTL': None,
    'AUTO_REFRESH': False,
    'USER_SERIALIZER': 'apps.users.serializers.UserSerializer'
}

SPECTACULAR_SETTINGS = {
    'SCHEMA_PATH_PREFIX': r'/v[0-9]',
    'SERVE_INCLUDE_SCHEMA': False,
    'CAMELIZE_NAMES': True,
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'persistAuthorization': True,
        'displayOperationId': True,
    },
    'SCHEMA_COMPONENTS': {
        'securitySchemes': {
            'Bearer Token': {
                'type': 'http',
                'scheme': 'bearer',
                'bearerFormat': 'JWT',
            }
        }
    }
}

'''
if not config('DOC_ALLOW_ALL', default=False, cast=bool):
    SPECTACULAR_SETTINGS['SERVE_PERMISSIONS'] = (
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser',
    )
    SPECTACULAR_SETTINGS['SERVE_AUTHENTICATION'] = (
        'rest_framework.authentication.SessionAuthentication',
    )
'''

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CLEANUP_IGNORE_MEDIA_ROOT = True

ROOT_URLCONF = 'django_example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'django_example.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

database_settings = config.get('DATABASE_SETTINGS', {})

'''
DATABASES = {
    'default': {
        'ENGINE': database_settings.get('ENGINE', 'django.db.backends.postgresql'),
        'NAME': database_settings.get('NAME'),
        'USER': database_settings.get('USER', 'postgres'),
        'PASSWORD': database_settings.get('PASSWORD', ''),
        'HOST': database_settings.get('HOST', '127.0.0.1'),
        'PORT': database_settings.get('PORT', '5432')
    },
    'test': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

AUTH_USER_MODEL = 'users.User'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

LANGUAGES = [
    ('en', 'English'),
    ('es', 'Español')
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

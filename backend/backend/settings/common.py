import os
import sys

TEST = 'test' in sys.argv
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def path(*a):
    return os.path.join(BASE_DIR, *a)


# This trick allows to import apps without that prefixes
sys.path.insert(0, path('apps'))
sys.path.insert(1, path('.'))


DEBUG = True
ALLOWED_HOSTS = [
    '192.168.0.%s' % i for i in range(255)
]
ROOT_URLCONF = 'backend.urls'
WSGI_APPLICATION = 'backend.wsgi.application'


AUTH_USER_MODEL = 'auth.User'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_extensions',
    'corsheaders',

    'budget',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'corsheaders.middleware.CorsMiddleware',
]
# -----------------------------------------------------------------------------


# CORS =====-------------------------------------------------------------------
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]
# -----------------------------------------------------------------------------


# TEMPLATES -------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [path('templates')],
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
# -----------------------------------------------------------------------------


# DATABASES --------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# ------------------------------------------------------------------------------


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


# INTERNATIONALIZATION --------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    path('static'),
]
# -----------------------------------------------------------------------------


# INTERNATIONALIZATION --------------------------------------------------------
TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# -----------------------------------------------------------------------------


# REST_FRAMEWORK --------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',  # NOQA
    'PAGE_SIZE': 20,
    'COERCE_DECIMAL_TO_STRING': False,
}
# -----------------------------------------------------------------------------


# IPYTHON NOTEBOOK ------------------------------------------------------------
IPYTHON_ARGUMENTS = [
    '--ext', 'django_extensions.management.notebook_extension',
]
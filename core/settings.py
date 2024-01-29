"""Global Project Configurations."""

from pathlib import Path
import os
import sys
import environ


# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent


# Environment Variable settings
env = environ.Env()
environ.Env.read_env()

ENVIRONMENT = env
SECRET_KEY = os.environ.get('SECRET_KEY')


# DEBUG settings: FALSE in production
DEBUG = 'RENDER' not in os.environ


# Host permission settings
ALLOWED_HOSTS = [
    '*'
]


# Render settings
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Installed Apps categories
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CORE_APPS = [
    'users',
    'core',
    'home',
    'products',
    'cart',
    'management',
    'payment',
]

THIRD_PARTY_APPS = [
    'paypal.standard.ipn',
    'import_export',
]

INSTALLED_APPS = DJANGO_APPS + CORE_APPS + THIRD_PARTY_APPS


SITE_ID = 1


# Paypal settings
PAYPAL_RECEIVER_EMAIL = 'sb-bjeh4728354490@business.example.com' # Sandbox email
PAYPAL_TEST = True
PAYPAL_BUY_BUTTON_IMAGE = '/static/img/buttom_paypal.svg'


# Auth model settings
AUTH_USER_MODEL = 'users.CustomUser'


# Log setting
LOGIN_URL = '/users/login/'


# NPM
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"


AUTHENTICATION_BACKENDS = [
    # Needed to log in by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL settings
ROOT_URLCONF = 'core.urls'


# Templates settings
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
                'utils.context_processors.company',
                'utils.context_processors.user_preferences',
                'utils.context_processors.products_featured',
                'utils.context_processors.products_categories',
                'utils.context_processors.cart_items_count',
            ],
        },
    },
]

# WSGI entry point
WSGI_APPLICATION = 'core.wsgi.application'


# Database settings
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
else:
    DATABASES = {
        "default": env.db("DATABASE_URL", default="postgres:///new_store"),
    }
    DATABASES["default"]["ATOMIC_REQUEST"] = True


PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

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

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static file settings
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')


# Media file settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

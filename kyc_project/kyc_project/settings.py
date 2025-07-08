from pathlib import Path
import os
import dj_database_url
 
# ----------------------------
# Base Directory
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
 
# ----------------------------
# Secret Key
# ----------------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-for-local')
 
# ----------------------------
# Debug Mode
# ----------------------------
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
 
# ----------------------------
# Allowed Hosts
# ----------------------------
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')
 
# ----------------------------
# Installed Apps
# ----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kyc_app',
    'whitenoise.runserver_nostatic',  # for serving static in prod
]
 
# ----------------------------
# Middleware
# ----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
 
# ----------------------------
# Root URLs & WSGI
# ----------------------------
ROOT_URLCONF = 'kyc_project.urls'
WSGI_APPLICATION = 'kyc_project.wsgi.application'
 
# ----------------------------
# Templates
# ----------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # if you use a global template dir
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
 
# ----------------------------
# Database
# ----------------------------
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        conn_max_age=600,
        ssl_require=not DEBUG
    )
}
 
# ----------------------------
# Password Validators
# ----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
 
# ----------------------------
# Internationalization
# ----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
 
# ----------------------------
# Static and Media Files
# ----------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'kyc_app/static']
 
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
 
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
 
# ----------------------------
# Auth Redirects
# ----------------------------
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
 
# ----------------------------
# Security for Production
# ----------------------------
if not DEBUG:
    CSRF_TRUSTED_ORIGINS = [f"https://{host}" for host in ALLOWED_HOSTS if host != '*']
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = True
 
# ----------------------------
# Default Auto Field
# ----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 

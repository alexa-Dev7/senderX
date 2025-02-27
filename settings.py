import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'daphne',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'channels',
    'sender',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'sender.urls'
ASGI_APPLICATION = 'sender.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    },
}

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']

DATA_FILE = os.path.join(BASE_DIR, 'data.json')
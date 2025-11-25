from .settings import *

DEBUG = False

# Your deployed domain on PythonAnywhere
ALLOWED_HOSTS = ['8714148445.pythonanywhere.com']

# Use SQLite for simplicity (or configure MySQL if needed)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # collectstatic will copy all static files here

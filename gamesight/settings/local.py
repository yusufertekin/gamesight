from gamesight.settings.base import *

DEBUG = True

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar', 
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

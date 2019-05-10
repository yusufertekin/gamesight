from gamesight.settings.base import *

DEBUG = True

INSTALLED_APPS += [
    'django_extensions',
    'debug_toolbar', 
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static/')

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

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

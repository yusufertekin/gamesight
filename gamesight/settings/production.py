from gamesight.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gamesight',
        'USER': 'gamesight',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static/')

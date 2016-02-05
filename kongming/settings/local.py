from kongming.settings.base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'chinese_db',
        'USER': 'chinese_user',
        'PASSWORD': 'chinese_pass',
        'HOST': 'localhost',
        'PORT': '5432',
        'CONN_MAX_AGE': 500
    }
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'
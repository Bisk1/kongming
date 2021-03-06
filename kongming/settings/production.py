from kongming.settings.base import *

import os
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'storages',
)

DATABASES = {'default': dj_database_url.config()}
DATABASES['default']['CONN_MAX_AGE'] = 500

# see http://developer.yahoo.com/performance/rules.html#expires
AWS_HEADERS = {
    'Cache-Control': 'max-age=86400',
}

AWS_PRELOAD_METADATA=True
AWS_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME=os.environ.get('AWS_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'kongming.custom_storages.StaticStorage'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
BASE_DEFAULT_FILE_STORAGE = 'kongming.custom_storages.MediaStorage'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

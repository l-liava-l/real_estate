from nedviga_backend.settings_base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

APPEND_SLASH = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nedviga',
        'HOST': '192.168.10.1',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'raw_type_999',
    }
}

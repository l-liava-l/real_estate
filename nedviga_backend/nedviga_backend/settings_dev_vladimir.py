from nedviga_backend.settings_dev import *

APPEND_SLASH = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nedviga',
        'USER': 'nedviga',
        'PASSWORD': 'nedviga',
    }
}

DEBUG = True

TEMPLATE_DEBUG = DEBUG

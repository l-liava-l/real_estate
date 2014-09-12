from nedviga_backend.settings_dev import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nedviga',
        'USER': 'postgres',
        'PASSWORD': 'qq',
    }
}
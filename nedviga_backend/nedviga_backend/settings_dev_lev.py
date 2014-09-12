from nedviga_backend.settings_dev import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'nedviga.sqlite3'),
    }
}
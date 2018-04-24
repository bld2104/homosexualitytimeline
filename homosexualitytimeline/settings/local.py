from .base import *

[t.get('OPTIONS').update({'debug': True}) for t in TEMPLATES] # noqa

DEBUG = True
SECRET_KEY = 'asdfasdfasdf'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
from .base import *
from decouple import config
import dj_database_url


DEBUG = False

SECRET_KEY = 'asdfasdf'

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

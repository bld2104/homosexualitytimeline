from .base import *
# from decouple import config
import dj_database_url


DEBUG = False

SECRET_KEY = 'asdfasdfasdojadsoifjadsoifj'

# DATABASES = {
#     'default': dj_database_url.config(
#         default=config('DATABASE_URL')
#     )
# }


db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

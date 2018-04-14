release: python manage.py migrate --settings homosexualitytimeline.settings.production

web: gunicorn homosexualitytimeline.wsgi:application --preload --workers 1

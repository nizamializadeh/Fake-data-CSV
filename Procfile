release: python manage.py migrate
web: gunicorn fakery.wsgi
worker: celery -A fakery.celery worker -B --loglevel=info


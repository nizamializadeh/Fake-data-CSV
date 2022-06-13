1.python3 -m venv .venv

2.source venv/bin/activate

3.pip3 install -r requirements.txt

4.celery -A fakery.celery worker -B --loglevel=info

5.python3 manage.py runserver


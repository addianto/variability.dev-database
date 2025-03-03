#!/bin/sh 
 
while ! nc -zv db 5432; do echo "Connecting" && sleep 1; done; 
 
python manage.py makemigrations 
# python manage.py migrate --run-syncdb 
python manage.py migrate
python manage.py seed_licenses ./core/fileupload/management/commands/file_seeds 1 1 1 
gunicorn --bind ":8000" --workers 3 ddueruemweb.wsgi:application 
 

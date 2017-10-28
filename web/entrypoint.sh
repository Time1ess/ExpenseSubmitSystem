#!/bin/bash
echo "Initializing Django server"
cd ExpenseSubmitSystem
echo "Pulling new changes from git repository"
git pull
echo "Installing requirements"
pip install -r requirements.txt
echo "Collecting static files"
python manage.py collectstatic -c --noinput
echo "Make migrations"
python manage.py makemigrations
echo "Migrating databases"
python manage.py migrate
echo "Compiling messages"
python manage.py compilemessages
echo "Starting uwsgi"
uwsgi --ini web/ExpenseSubmitSystem_uwsgi.ini

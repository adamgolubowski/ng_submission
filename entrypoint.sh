#!/bin/bash
echo "Apply database migrations"
python manage.py migrate --run-syncdb
echo "Starting server"
python manage.py runserver 0.0.0.0:8000

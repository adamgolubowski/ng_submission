echo "Apply database migrations"
python manage.py migrate --run-syncdb
echo "Starting server"
gunicorn ng_solution.wsgi --log-file -

web: python manage.py migrate --no-input && python manage.py collectstatic --no-input && gunicorn kyc_project.wsgi:application --bind 0.0.0.0:$PORT

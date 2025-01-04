release: python manage.py makemigrations && python manage.py migrate && python manage.py create_superadmin
web: gunicorn fictious_candle.wsgi:application --log-file -

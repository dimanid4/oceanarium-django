#!/usr/bin/env bash
set -e

echo "=== Running migrations ==="
python manage.py migrate --noinput

echo "=== Creating superuser (if not exists) ==="
python manage.py createsuperuser --noinput || true

echo "=== Collecting static files ==="
python manage.py collectstatic --noinput

echo "=== Starting Gunicorn ==="
gunicorn aquarium.wsgi:application

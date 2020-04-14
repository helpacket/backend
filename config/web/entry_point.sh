#!/usr/bin/env bash

python manage.py collectstatic --no-input

python manage.py migrate

if [ "$ENVIRONMENT" = "DEVELOPMENT" ]
then
  gunicorn _setup.wsgi -b 0.0.0.0:8000 --reload
else
  gunicorn _setup.wsgi -b 0.0.0.0:8000
fi

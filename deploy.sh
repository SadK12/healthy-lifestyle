#!/bin/bash

poetry install
poetry run ./healthcare/manage.py migrate
poetry run ./healthcare/manage.py collectstatic -c --noinput
poetry run ./healthcare/manage.py check --deploy

sudo systemctl restart django_2022_healthcare.service

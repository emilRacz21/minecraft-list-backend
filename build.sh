#!/usr/bin/env bash
cd new
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input

#!/bin/bash

cd /usr/src/app/

python manage.py migrate
python manage.py runserver 0.0.0.0:5001
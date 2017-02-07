#!/usr/bin/env bash

read -p "DB admin username: " user
read -s -p "DB admin password: " pass

PGPASSWORD=$pass psql -U $user < recreate_db.sql

cd ..
./manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'abcdef')" | python manage.py shell
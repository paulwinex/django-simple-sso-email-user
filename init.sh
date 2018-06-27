#!/usr/bin/env bash

echo "=========== MIGRATE ============="
./manage.py makemigrations account
./manage.py migrate
echo "=========== COLLECT STATIC ==========="
./manage.py collectstatic --noinput
echo "=========== INIT SCRIPTS ==========="
./manage.py shell < super.py
echo "=========== INIT SSO ==========="
./manage.py shell < init_sso.py

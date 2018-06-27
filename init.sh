#!/usr/bin/env bash

rm /tmp/server_db.sqlite3
echo "=========== MIGRATE ============="
./manage.py makemigrations account
./manage.py migrate
echo "=========== COLLECT STATIC ==========="
./manage.py collectstatic --noinput
echo "=========== INIT SCRIPTS ==========="
./manage.py shell < super.py
echo "=========== INIT SSO ==========="
./manage.py shell < init_sso.py

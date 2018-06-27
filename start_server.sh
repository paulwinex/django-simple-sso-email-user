#!/usr/bin/env bash

source ././../env/bin/activate
export IS_SSO_SERVER=1
./manage.py runserver 0.0.0.0:8000

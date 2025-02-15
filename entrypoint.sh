#!/usr/bin/env bash


gunicorn_path=$(which gunicorn)

if [[ $gunicorn_path == "" ]]; then
    . ../env/bin/activate
fi


mkdir -p logs
mkdir -p staticfiles


chown www-data:www-data staticfiles
./manage.py collectstatic --noinput
cp -v templates/favicon.ico staticfiles

gunicorn armyibaform.wsgi 8000 &
disown %1


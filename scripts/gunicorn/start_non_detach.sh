#!/bin/bash

DJANGO_SETTINGS=pyconph.settings
DJANGO_WSGI=pyconph.wsgi
SOCKFILE=/srv/funny/pycon2018/run/gunicorn.sock
PIDFILE=/srv/funny/pycon2018/run/gunicorn.pid
LOG_FILE=/srv/funny/pycon2018/logs/gunicorn.log
LOG_LEVEL=debug
NUM_WORKERS=3

# Delete any existing sock and pid files
rm -f $PIDFILE $SOCKFILE

echo "-> Starting gunicorn:edgepi as user funny"
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS
export PYTHONPATH=/srv/funny/pycon2018:\$PYTHONPATH
exec gunicorn \
    ${DJANGO_WSGI}:application \
    --name happy \
    --user funny \
    --group funny \
    --workers $NUM_WORKERS \
    --bind=unix:$SOCKFILE \
    --log-level=$LOG_LEVEL \
    --log-file=$LOG_FILE \
    --pid=$PIDFILE \

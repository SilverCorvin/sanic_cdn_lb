#!/bin/sh
set -e

if [ "$1" = 'run_app' ]; then
    exec gunicorn -c conf/gunicorn.conf.py main:app
fi

exec $@

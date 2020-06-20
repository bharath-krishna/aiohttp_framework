#!/usr/bin/env sh
export PYTHONPATH=${APP_DIR}

gunicorn -c gunicorn_config.py app:app
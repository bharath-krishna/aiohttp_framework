#!/usr/bin/env sh
export PYTHONPATH=${APP_DIR}

python -m app --host ${HOST} --port ${PORT}
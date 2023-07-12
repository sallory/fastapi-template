#! /usr/bin/env sh
set -e

/prestart.sh

APP_MODULE=${APP_MODULE:-"src.main:app"}

echo "STARTING WITH RELOAD"

uvicorn "$APP_MODULE" --host 0.0.0.0 --port 8000 --reload
#!/bin/bash
if test "x${APPNAME}" = "xappappurlshortner" ; then
  gunicorn --log-level debug --reload --bind 0.0.0.0:8080 --timeout=15 --worker-class=uvicorn.workers.UvicornWorker --keep-alive 60 --workers 4 appurlshortner.web:app
else
  echo "Invalid \$APPNAME '${APPNAME}'"
  exit 1
fi
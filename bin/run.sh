#!/bin/bash
if test "x${APPNAME}" = "xappappurlshortener" ; then
  gunicorn --log-level debug --reload --bind 0.0.0.0:8080 --timeout=15 --worker-class=uvicorn.workers.UvicornWorker --keep-alive 60 --workers 4 appurlshortener.web:app
else
  echo "Invalid \$APPNAME '${APPNAME}'"
  exit 1
fi
#!/bin/bash
if test "x${APPNAME}" = "xappappurlurl_shortener" ; then
  gunicorn --log-level debug --reload --bind 0.0.0.0:8080 --timeout=15 --worker-class=uvicorn.workers.UvicornWorker --keep-alive 60 --workers 4 appurlurl_shortener.web:app
else
  echo "Invalid \$APPNAME '${APPNAME}'"
  exit 1
fi
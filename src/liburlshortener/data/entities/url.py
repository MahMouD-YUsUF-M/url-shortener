from jsql import sql

from liburlshortener.data.models import tables
from libutil.sqlutil import insert_row


def insert_url(conn, id_user, url_code, expires_at, target_url):
    row = {'id_user': id_user, 'url_code': url_code, 'expires_at': expires_at, 'target_url': target_url}

    insert_row(conn, tables.Url, row)

    return {"url_code": url_code, 'expires_at': expires_at}


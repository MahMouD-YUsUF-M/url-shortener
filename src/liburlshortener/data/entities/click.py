from liburlshortener.data.models import tables
from libutil.sqlutil import insert_row


def insert_click(conn, id_url):
    row = {"id_url": id_url}

    insert_row(conn, tables.Click, row)

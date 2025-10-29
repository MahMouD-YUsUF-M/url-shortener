from jsql import sql

from liburlshortener.data.models import tables
from libutil.sqlutil import insert_row


def get_id_by_code(conn, user_code):
    return sql(
        conn,
        '''
        SELECT id_user
        FROM user
        WHERE user_code=:user_code
    ''',
        user_code=user_code,
    ).scalar()


def insert_user(conn, code):
    id_user = insert_row(conn, tables.User, {'user_code': code, "is_guest": True}).lastrowid
    return id_user

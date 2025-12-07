from jsql import sql

from liburlshortener.data.models import tables
from libutil.sqlutil import insert_row


def insert_url(conn, id_user, url_code, expires_at, target_url):
    row = {'id_user': id_user, 'url_code': url_code, 'expires_at': expires_at, 'target_url': target_url}

    insert_row(conn, tables.Url, row)

    return {"url_code": url_code, 'expires_at': expires_at}


def check_url_code_exists(conn, url_code):
    code = sql(
        conn,
        '''
        SELECT url_code
        FROM url
        WHERE url_code = :url_code
        ''',
        url_code=url_code,
    ).scaler()

    return code is not None


def get_all_user_urls(conn, id_user):
    return sql(
        conn,
        '''
        SELECT u.url_code,
               u.expires_at,
               u.target_url,
               u.id_url,
               COALESCE(COUNT(c.id_click), 0) as click_count
        FROM url AS u
                 LEFT JOIN click AS c ON c.id_url = u.id_url
        WHERE u.id_user = :id_user
          AND u.expires_at > NOW()
        GROUP BY u.id_url, u.url_code, u.expires_at, u.target_url;
        ''',
        id_user=id_user,
    ).dicts()


def get_url_by_code(conn, url_code):
    return sql(
        conn,
        '''
        SELECT target_url,
               expires_at,
               id_url

        FROM url

        WHERE url_code = :url_code
        ''',
        url_code=url_code,
    ).dict()

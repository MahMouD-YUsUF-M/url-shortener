from jsql import sql

from liburlshortener.data.models import tables
from libutil.sqlutil import insert_row


def insert_url(conn, id_user, url_code, expires_at, target_url):
    row = {'id_user': id_user, 'url_code': url_code, 'expires_at': expires_at, 'target_url': target_url}

    insert_row(conn, tables.Url, row)

    return {"url_code": url_code, 'expires_at': expires_at}


def get_all_user_urls(conn, id_user):
    return sql(
        conn,
        '''
      SELECT u.url_code,
       u.expires_at,
       u.target_url,
       u.id_url,
       COALESCE(c.click_count, 0) as click_count
FROM url AS u
         LEFT JOIN (SELECT id_url, COUNT(*) as click_count
                    FROM click
                    WHERE id_url IN 
                          (SELECT id_url
                                     FROM url
                                     WHERE id_user = :id_user
                                       AND expires_at > NOW())
                    GROUP BY id_url) 
                                    AS c ON c.id_url = u.id_url
WHERE u.id_user = :id_user
  AND u.expires_at > NOW();
        ''',
        id_user=id_user,
    ).dicts()


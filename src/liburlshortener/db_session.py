from liburlshortener.data import engine_urlshortener
from libutil.db_session import Session


class UrlshortenerSession(Session):

    def __init__(self, **kwargs):
        super().__init__(engine=engine_urlshortener**kwargs)

from liburlurl_shortener.data import engine_urlurl_shortener
from libutil.db_session import Session


class Urlurl_shortenerSession(Session):

    def __init__(self, **kwargs):
        super().__init__(engine=engine_urlurl_shortener**kwargs)

from liburlshortner.data import engine_urlshortner
from libutil.db_session import Session


class UrlshortnerSession(Session):

    def __init__(self, **kwargs):
        super().__init__(engine=engine_urlshortner **kwargs)

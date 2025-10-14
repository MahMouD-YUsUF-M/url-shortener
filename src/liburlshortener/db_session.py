from liburl_shortener.data import engine_url_shortener
from libutil.db_session import Session


class url_shortenerSession(Session):

    def __init__(self, **kwargs):
        super().__init__(engine=engine_url_shortener**kwargs)

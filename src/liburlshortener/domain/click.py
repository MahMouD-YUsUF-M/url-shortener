from libutil.util import BaseModel
from liburlshortener.data import entities


class AddClick(BaseModel):

    def execute(self, session, id_url):
        entities.click.insert_click(session.conn, id_url)

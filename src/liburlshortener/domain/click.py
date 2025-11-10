from liburlshortener.data import entities
from libutil.util import BaseModel


class AddClick(BaseModel):
    id_url: int

    def execute(self, session):
        entities.click.insert_click(session.conn, self.id_url)

from liburl_shortener.data import engine_url_shortener
from libutil import util
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_all():
    Base.metadata.create_all(engine_url_shortener)


def recreate_all():
    assert util.IS_DEV, 'must be dev'
    Base.metadata.drop_all(engine_url_shortener)
    Base.metadata.create_all(engine_url_shortener)


class Model(Base):
    __abstract__ = True
    __bind_key__ = 'url_shortener'


TINYINT = mysql.TINYINT(unsigned=True)
SMALLINT = mysql.SMALLINT(unsigned=True)
MEDIUMINT = mysql.MEDIUMINT(unsigned=True)
INT = mysql.INTEGER(unsigned=True)
BIGINT = mysql.BIGINT(unsigned=True)
SINT = mysql.INTEGER(unsigned=False)
SBIGINT = mysql.BIGINT(unsigned=False)

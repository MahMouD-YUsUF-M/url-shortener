from liburlshortener.data import engine_urlshortener
from libutil import util
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_all():
    Base.metadata.create_all(engine_urlshortener)


def recreate_all():
    assert util.IS_DEV, 'must be dev'
    Base.metadata.drop_all(engine_urlshortener)
    Base.metadata.create_all(engine_urlshortener)


class Model(Base):
    __abstract__ = True
    __bind_key__ = 'urlshortener'


TINYINT = mysql.TINYINT(unsigned=True)
SMALLINT = mysql.SMALLINT(unsigned=True)
MEDIUMINT = mysql.MEDIUMINT(unsigned=True)
INT = mysql.INTEGER(unsigned=True)
BIGINT = mysql.BIGINT(unsigned=True)
SINT = mysql.INTEGER(unsigned=False)
SBIGINT = mysql.BIGINT(unsigned=False)

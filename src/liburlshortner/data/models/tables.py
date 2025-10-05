from liburlshortner.data import engine_urlshortner
from libutil import util
from sqlalchemy.dialects import mysql
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_all():
    Base.metadata.create_all(engine_urlshortner)


def recreate_all():
    assert util.IS_DEV, 'must be dev'
    Base.metadata.drop_all(engine_urlshortner)
    Base.metadata.create_all(engine_urlshortner)


class Model(Base):
    __abstract__ = True
    __bind_key__ = 'urlshortner'


TINYINT = mysql.TINYINT(unsigned=True)
SMALLINT = mysql.SMALLINT(unsigned=True)
MEDIUMINT = mysql.MEDIUMINT(unsigned=True)
INT = mysql.INTEGER(unsigned=True)
BIGINT = mysql.BIGINT(unsigned=True)
SINT = mysql.INTEGER(unsigned=False)
SBIGINT = mysql.BIGINT(unsigned=False)

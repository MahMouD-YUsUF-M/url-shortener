import sqlalchemy as sa
from liburlshortner.data import engine_urlshortner
from libutil import util
from sqlalchemy import text, types
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
INT = mysql.INTEGER(unsigned=True)d
BIGINT = mysql.BIGINT(unsigned=True)
SINT = mysql.INTEGER(unsigned=False)
SBIGINT = mysql.BIGINT(unsigned=False)


class User(Model):
    __tablename__ = 'user'

    id_user = sa.Column(sa.BIGINT, primary_key=True)
    user_code = sa.Column(sa.String(50), nullable=False, unique=True)
    is_guest = sa.Column(sa.Boolean, nullable=False ,server_default=sa.sql.expression.true())

    created_at = sa.Column(types.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False)

    updated_at = sa.Column(
        types.TIMESTAMP,
        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
        nullable=False,
    )


class Url(Model):
    __tablename__ = 'url'
    id_url = sa.Column(sa.BIGINT, primary_key=True)
    url_code = sa.Column(sa.String(7), nullable=False, unique=True)

    target_url = sa.Column(sa.String(255), nullable=False, index=True)
    id_user = sa.Column(sa.BIGINT, nullable=False, index=True)
    expires_at = sa.Column(
        types.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP + INTERVAL 30 DAY'), nullable=False, index=True
    )

    created_at = sa.Column(types.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False, index=True)

    updated_at = sa.Column(
        types.TIMESTAMP,
        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
        nullable=False,
    )


class Click(Model):
    __tablename__ = 'click'
    id_click = sa.Column(sa.BIGINT, primary_key=True)
    id_url = sa.Column(sa.BIGINT, nullable=False, index=True)
    created_at = sa.Column(types.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), nullable=False, index=True)
    updated_at = sa.Column(
        types.TIMESTAMP,
        server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
        nullable=False
    )

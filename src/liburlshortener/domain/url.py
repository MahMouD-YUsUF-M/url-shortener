from datetime import datetime, timedelta
from pydantic import field_validator

from liburlshortener.exceptions import UrlValidationException
from libutil.util import BaseModel
from liburlshortener.data import entities
import validators
from liburlshortener.domain import constants
import random
import string


def generate_url_code():
    valid_chars = string.ascii_letters + string.digits
    url_code = ''.join(random.choice(valid_chars) for _ in range(8))
    return url_code


class AddUrl(BaseModel):
    target_url: str

    @field_validator('target_url')
    def validate_target_url(cls, url: str) -> str:
        if not validators.url(url):
            raise ValueError('Invalid URL')
        return url

    def execute(self, ctx, session):
        url_code = generate_url_code()
        target_url = self.target_url
        expires_at = datetime.now() + timedelta(days=constants.URL_EXPIRATION_DAYS)
        url_row = entities.url.insert_url(
            session.conn,
            ctx.id_user,
            url_code,
            expires_at,
            target_url,
        )
        return url_row


class GetUrl(BaseModel):

    def execute(self, ctx, session):
        urls = entities.url.get_all_user_urls(session.conn, ctx.id_user)

        return urls


class GetUrlByCode(BaseModel):
    short_code: str

    def execute(self, ctx, session):
        url_info = entities.url.get_url_by_code(session.conn, ctx.id_user, self.short_code)

        if url_info is None:
            raise UrlValidationException(f"Invalid url code: {self.short_code}")

        if url_info['expires_at'] < datetime.now():
            raise UrlValidationException(f"Short code {self.short_code} expired")

        return {'target_url': url_info['target_url'], 'id_url': url_info['id_url']}

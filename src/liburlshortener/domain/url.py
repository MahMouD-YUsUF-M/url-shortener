import random
import string
from datetime import datetime, timedelta
from urllib.parse import urlparse

from pydantic import field_validator

from liburlshortener.data import entities
from liburlshortener.domain import constants
from liburlshortener.exceptions import UrlNonExistingException, CodeNotFoundException
from libutil.util import BaseModel


def generate_url_code():
    valid_chars = string.ascii_letters + string.digits
    url_code = ''.join(random.choice(valid_chars) for _ in range(constants.URL_CODE_LENGTH))
    return url_code


class AddUrl(BaseModel):
    target_url: str

    @field_validator('target_url')
    def validate_target_url(cls, url: str) -> str:
        parsed_url = urlparse(url)

        if not parsed_url.scheme or not parsed_url.netloc:
            raise ValueError('URL is not valid')

        if parsed_url.scheme not in ['http', 'https']:
            raise ValueError('URL scheme must be http or https')

        return url

    def execute(self, ctx, session):
        is_unique_code = False
        url_code = ""

        for i in range(1, 5):
            url_code = generate_url_code()
            is_unique_code = entities.url.is_url_code_exists(conn=session.conn, url_code=url_code)
            if not is_unique_code:
                break

        if is_unique_code:
            raise CodeNotFoundException("Can't generate short url ")

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


class GetUrls(BaseModel):

    def execute(self, ctx, session):
        urls = entities.url.get_all_user_urls(session.conn, ctx.id_user)

        return urls


class GetUrlByCode(BaseModel):
    short_code: str

    def execute(self, session):
        url_info = entities.url.get_url_by_code(session.conn, self.short_code)

        if url_info is None:
            raise UrlNonExistingException(f"Invalid url code: {self.short_code}")

        if url_info['expires_at'] < datetime.now():
            raise UrlNonExistingException(f"Short code {self.short_code} expired")

        return {'target_url': url_info['target_url'], 'id_url': url_info['id_url']}

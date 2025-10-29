from datetime import datetime
from typing import List

from liburlshortener.messages.common import ResponseBaseModel
from libutil.util import BaseModel
from liburlshortener.messages import constants


class ShortUrl(BaseModel):
    short_url: str
    expire_at: datetime


class ShortenUrlResponse(ResponseBaseModel):
    data: ShortUrl
def shorten_url_format(row):
    short_url_info = ShortUrl(
        short_url=constants.Prefix_for_url + row["url_code"],
        expire_at=(row["expires_at"]),
    )
    return short_url_info


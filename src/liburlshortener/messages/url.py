from datetime import datetime
from typing import List

from liburlshortener.messages.common import ResponseBaseModel
from libutil.util import BaseModel


class ShortUrl(BaseModel):
    short_url: str
    expire_at: datetime


class ShortUrlGet(BaseModel):
    short_url: str
    expire_at: datetime
    target_url: str
    clicks: int


class ShortUrlGetList(BaseModel):
    shorturls: List[ShortUrlGet]


class ShortenUrlResponse(ResponseBaseModel):
    data: ShortUrl


class ShortenUrlGetResponse(ResponseBaseModel):
    data: ShortUrlGetList


def shorten_url_format(row, request):
    short_url_info = ShortUrl(
        short_url=str(request.url_for('redirect_url', short_code=row["url_code"])),
        expire_at=(row["expires_at"]),
    )
    return short_url_info


def shorten_url_get_format(rows, request):

    short_urls_info = ShortUrlGetList(shorturls=[])

    for short_url_info in rows:
        short_urls_info.shorturls.append(
            ShortUrlGet(
                expire_at=short_url_info["expires_at"],
                target_url=short_url_info["target_url"],
                clicks=short_url_info["click_count"],
                short_url=str(request.url_for('redirect_url', short_code=short_url_info["url_code"])),
            )
        )

    return short_urls_info

from datetime import datetime
from typing import List

from liburlshortener.messages.common import ResponseBaseModel
from libutil.util import BaseModel
from liburlshortener.messages import constants


class ShortUrl(BaseModel):
    short_url: str
    expire_at: datetime


class ShortUrlGet(BaseModel):
    short_url: str
    expire_at: datetime
    target_url: str
    clicks: int


class ShortUrlGetList(BaseModel):
    ShortUrl: List[ShortUrlGet]


class ShortenUrlResponse(ResponseBaseModel):
    data: ShortUrl


class ShortenUrlGetResponse(ResponseBaseModel):
    data: ShortUrlGetList


def shorten_url_format(row):
    short_url_info = ShortUrl(
        short_url=constants.Prefix_for_url + row["url_code"],
        expire_at=(row["expires_at"]),
    )
    return short_url_info


def shorten_url_get_format(row):
    temp = []

    short_urls_info = ShortUrlGetList(ShortUrl=temp)

    for short_url_info in row:
        short_urls_info.ShortUrl.append(
            ShortUrlGet(
                expire_at=short_url_info["expires_at"],
                target_url=short_url_info["target_url"],
                clicks=short_url_info["click_count"],
                short_url=constants.Prefix_for_url + short_url_info["url_code"],
            )
        )

    return short_urls_info

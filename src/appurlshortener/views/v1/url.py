from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi.params import Depends

from liburlshortener import domain
from liburlshortener.context import RequestContext
from liburlshortener.db_session import UrlShortenerSession
from liburlshortener.messages.url import (
    ShortenUrlResponse,
    shorten_url_format,
    shorten_url_get_format,
    ShortenUrlGetResponse,
)
from appurlshortener.views.v1.dependencies import get_request_context

router = APIRouter()


@router.post('/')
def shorten_url(msg: domain.url.AddUrl, ctx: RequestContext = Depends(get_request_context)):
    with UrlShortenerSession() as session:
        short_url_info = shorten_url_format(msg.execute(ctx, session))

    return ShortenUrlResponse(success=True, data=short_url_info)


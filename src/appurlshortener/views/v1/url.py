from fastapi import APIRouter
from fastapi import Request
from fastapi.params import Depends
from fastapi.responses import RedirectResponse

from appurlshortener.views.v1.dependencies import get_request_context
from liburlshortener import domain
from liburlshortener.context import RequestContext
from liburlshortener.db_session import UrlShortenerSession
from liburlshortener.messages.url import (
    ShortenUrlResponse,
    shorten_url_format,
    shorten_url_get_format,
    ShortenerUrlsGetResponse,
)

router = APIRouter()


@router.post('/')
def shorten_url(msg: domain.url.AddUrl, request: Request, ctx: RequestContext = Depends(get_request_context)):
    with UrlShortenerSession() as session:
        url_info = msg.execute(ctx, session)
        short_url_info = shorten_url_format(url_info, request)

    return ShortenUrlResponse(success=True, data=short_url_info)


@router.get('/')
def get_urls(request: Request, ctx: RequestContext = Depends(get_request_context)):
    with UrlShortenerSession() as session:
        urls = domain.url.GetUrls().execute(ctx, session)
        urls_info = shorten_url_get_format(urls, request)

    return ShortenerUrlsGetResponse(success=True, data=urls_info)


@router.get('/{short_code}', name='redirect_url')
def redirect_url(msg: domain.url.GetUrlByCode = Depends()):
    with UrlShortenerSession() as session:
        url_info = msg.execute(session)
        domain.click.AddClick(id_url=url_info['id_url']).execute(session)
        return RedirectResponse(url_info['target_url'], status_code=307)

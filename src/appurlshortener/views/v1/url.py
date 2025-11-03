from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi.params import Depends
from fastapi import Request
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
def shorten_url(msg: domain.url.AddUrl, request: Request, ctx: RequestContext = Depends(get_request_context)):
    with UrlShortenerSession() as session:
        short_url_info = shorten_url_format(msg.execute(ctx, session), request)

    return ShortenUrlResponse(success=True, data=short_url_info)


@router.get('/')
def get_urls(request: Request, ctx: RequestContext = Depends(get_request_context)):
    with UrlShortenerSession() as session:
        urls = shorten_url_get_format(domain.url.GetUrls().execute(ctx, session), request)

    return ShortenUrlGetResponse(success=True, data=urls)


@router.get('/{short_url}', name='redirect_url')
def redirect_url(msg: domain.url.GetUrlByCode = Depends(), ctx: RequestContext = Depends(get_request_context)):
    with UrlShortenerSession() as session:
        url_info = msg.execute(ctx, session)
        domain.click.AddClick().execute(session, url_info['id_url'])

        return RedirectResponse(url_info['target_url'])

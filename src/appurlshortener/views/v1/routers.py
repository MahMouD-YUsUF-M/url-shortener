from fastapi import APIRouter

from . import url

router = APIRouter()
router.include_router(url.router, prefix='/urls', tags=['url'])

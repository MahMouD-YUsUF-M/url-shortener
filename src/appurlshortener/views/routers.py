from fastapi import APIRouter

from .system import router as system_router
from .v1.routers import router as router_v1

router = APIRouter()
router.include_router(system_router, tags=['system'])
router.include_router(router_v1, prefix='/v1')

from fastapi import APIRouter

from core import config
from .v1 import router as v1_router

router = APIRouter(prefix=config.api.prefix)

router.include_router(v1_router)

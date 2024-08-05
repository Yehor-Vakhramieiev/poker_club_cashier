from fastapi import APIRouter

from .players import router as players_router

router = APIRouter(prefix="/v1")

router.include_router(players_router)

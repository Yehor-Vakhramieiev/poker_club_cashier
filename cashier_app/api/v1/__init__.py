from fastapi import APIRouter

from .game import router as game_router
from .players import router as players_router

router = APIRouter(prefix="/v1")

router.include_router(players_router)
router.include_router(game_router)

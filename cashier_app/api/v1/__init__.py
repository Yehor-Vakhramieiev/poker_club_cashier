from fastapi import APIRouter

from core import config
from .club import router as club_router
from .game import router as game_router
from .players import router as players_router

router = APIRouter(prefix=config.api.v1.prefix)

router.include_router(players_router)
router.include_router(game_router)
router.include_router(club_router)

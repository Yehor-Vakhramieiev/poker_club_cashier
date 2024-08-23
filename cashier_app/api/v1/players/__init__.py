from fastapi import APIRouter
from .players import router as players_router
from .sessions import router as sessions_router
from .cash_operations import router as cash_operations_router

router = APIRouter()

players_router.include_router(sessions_router)
players_router.include_router(cash_operations_router)

router.include_router(players_router)

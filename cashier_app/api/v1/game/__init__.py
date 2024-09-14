from fastapi import APIRouter

from .table import router as table_session_router

router = APIRouter(prefix="/game")
router.include_router(table_session_router)


@router.get("")
async def get_game_session(): ...


@router.post("")
async def add_game_session(): ...


@router.patch("")
async def update_game_session(): ...


@router.get("/{id}")
async def get_game_session_detail(id: int): ...

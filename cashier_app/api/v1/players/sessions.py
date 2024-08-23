from typing import Annotated, TYPE_CHECKING

from fastapi import APIRouter, Depends

from api.dependencies import get_player_service
from api.schemas import (
    PlayerSessionSchema,
    AddPlayerSessionSchema,
    UpdatePlayerSessionSchema,
)

if TYPE_CHECKING:
    from api.services import PlayerService

router = APIRouter(prefix="/sessions")


@router.get("", response_model=list[PlayerSessionSchema | None])
async def get_sessions(
    player_service: Annotated["PlayerService", Depends(get_player_service)]
):
    return await player_service.get_active_sessions()


@router.post("", response_model=PlayerSessionSchema)
async def add_session(
    session: AddPlayerSessionSchema,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.add_session(session)


@router.patch("")
async def update_session(
    session_id: int,
    update_values: UpdatePlayerSessionSchema,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.update_session(session_id, update_values)

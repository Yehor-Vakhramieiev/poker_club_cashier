from typing import Annotated, TYPE_CHECKING

from fastapi import APIRouter, Depends

from api.dependencies.database import get_player_service
from api.schemas import (
    PlayerSchema,
    AddPlayerSchema,
    UpdatePlayerSchema,
    PlayerSessionSchema,
    AddPlayerSessionSchema,
    UpdatePlayerSessionSchema,
)

if TYPE_CHECKING:
    from api.services import PlayerService

router = APIRouter(prefix="/players", tags=["Players"])


@router.get("", response_model=list[PlayerSchema | None])
async def get_players(
    player_service: Annotated["PlayerService", Depends(get_player_service)],
    limit: int | None = None,
    offset: int | None = None,
):
    return await player_service.get_players(limit, offset)


@router.post("", response_model=PlayerSchema)
async def add_player(
    player_to_add: AddPlayerSchema,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.add_player(player_to_add)


@router.get("/sessions", response_model=list[PlayerSessionSchema | None])
async def get_players(
    player_service: Annotated["PlayerService", Depends(get_player_service)]
):
    return await player_service.get_active_sessions()


@router.post("/sessions", response_model=PlayerSessionSchema)
async def get_players(
    session: AddPlayerSessionSchema,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.add_session(session)


@router.patch("/sessions/{session_id}")
async def get_players(
    session_id: int,
    update_values: UpdatePlayerSessionSchema,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.update_session(session_id, update_values)


@router.get("/{player_id}", response_model=PlayerSchema | None)
async def get_player(
    player_id: int,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.get_player_by_id(player_id)


@router.patch("/{player_id}")
async def get_player(
    player_id: int,
    update_values: UpdatePlayerSchema,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.update_player(player_id, update_values)

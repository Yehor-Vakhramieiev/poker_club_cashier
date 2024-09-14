from typing import Annotated, TYPE_CHECKING

from fastapi import APIRouter, Depends

from api.dependencies import get_player_service, PlayerSearchParams
from api.schemas import (
    PlayerSchema,
    AddPlayerSchema,
    UpdatePlayerSchema,
    PlayerDetailSchema,
)
from .credit_deposit import router as cash_operations_router
from .sessions import router as sessions_router

if TYPE_CHECKING:
    from api.services import PlayerService


router = APIRouter(prefix="/player", tags=["Players"])
router.include_router(sessions_router)
router.include_router(cash_operations_router)


@router.get("", response_model=list[PlayerSchema | None])
async def get_players(
    params: Annotated[PlayerSearchParams, Depends()],
    player_service: Annotated["PlayerService", Depends(get_player_service)],
    limit: int | None = None,
    offset: int | None = None,
):
    return await player_service.get_players(params, limit, offset)


@router.post("", response_model=PlayerSchema)
async def add_player(
    player_to_add: AddPlayerSchema,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.add_player(player_to_add)


@router.patch("")
async def update_player(
    player_id: int,
    update_values: UpdatePlayerSchema,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.update_player(player_id, update_values)


@router.get("/{player_id}", response_model=PlayerDetailSchema | None)
async def get_player_detail(
    player_id: int,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.get_player_detail(player_id)

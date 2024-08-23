from typing import Annotated, TYPE_CHECKING

from fastapi import APIRouter, Depends

from api.dependencies import get_player_service
from api.schemas import (
    AddCashInOutSchema,
    CashInOutSchema,
    UpdateCashInOutSchema,
)

if TYPE_CHECKING:
    from api.services import PlayerService

router = APIRouter(prefix="/operation")


@router.get("", response_model=list[CashInOutSchema | None])
async def get_operations(
    session_id: int,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.get_all_operations_in_session(session_id)


@router.post("", response_model=CashInOutSchema)
async def add_operation(
    operation: AddCashInOutSchema,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.add_operation(operation)


@router.patch("")
async def update_session(
    operation_id: int,
    update_values: UpdateCashInOutSchema,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.update_operation(operation_id, update_values)

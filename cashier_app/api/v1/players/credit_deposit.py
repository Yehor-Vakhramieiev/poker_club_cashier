from typing import TYPE_CHECKING, Annotated

from fastapi import APIRouter, Depends

from api.dependencies import get_player_service
from api.schemas import (
    AddCreditDepositSchema,
    CreditDepositSchema,
    UpdateCreditDepositSchema,
)

if TYPE_CHECKING:
    from api.services import PlayerService

router = APIRouter(prefix="/credit_deposit")


@router.post("", response_model=CreditDepositSchema)
async def add_credit_deposit(
    operation: AddCreditDepositSchema,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.add_credit_deposit_operation(operation)


@router.patch("")
async def update_credit_deposit(
    operation_id: int,
    update_values: UpdateCreditDepositSchema,
    player_service: Annotated["PlayerService", Depends(get_player_service)],
):
    return await player_service.update_credit_deposit_operation(
        operation_id, update_values
    )

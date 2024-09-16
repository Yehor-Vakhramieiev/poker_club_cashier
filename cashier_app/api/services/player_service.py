from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.controllers import Controller
    from api.dependencies import PlayerSearchParams
    from api.schemas import (
        AddPlayerSchema,
        UpdatePlayerSchema,
        UpdatePlayerSessionSchema,
        AddPlayerSessionSchema,
        AddCashInOutSchema,
        UpdateCashInOutSchema,
        AddCreditDepositSchema,
        UpdateCreditDepositSchema,
    )


class PlayerService:
    def __init__(self, player_controller: "Controller"):
        self.controller = player_controller

    async def add_player(self, player_to_add: "AddPlayerSchema"):
        return await self.controller.players.controller.add(
            **player_to_add.model_dump()
        )

    async def get_players(
        self,
        search_params: "PlayerSearchParams",
        limit: int | None,
        offset: int | None,
    ):
        return await self.controller.players.controller.get(
            limit=limit,
            offset=offset,
            **search_params.model_dump(exclude_none=True),
        )

    async def get_player_detail(self, player_id: int):
        return await self.controller.players.controller.get(player_id=player_id)

    async def update_player(self, player_id: int, update_values: "UpdatePlayerSchema"):
        await self.controller.players.controller.update(
            player_id,
            **update_values.model_dump(exclude_none=True),
        )

    async def add_session(self, session: "AddPlayerSessionSchema"):
        return await self.controller.players.sessions.add(**session.model_dump())

    async def get_active_sessions(self):
        return await self.controller.players.sessions.get()

    async def get_session_detail(self, session_id: int):
        return await self.controller.players.sessions.get(session_id=session_id)

    async def update_session(
        self, player_id: int, update_values: "UpdatePlayerSessionSchema"
    ):

        await self.controller.players.sessions.update(
            player_id,
            **update_values.model_dump(exclude_none=True),
        )

    async def add_operation(self, operation: "AddCashInOutSchema"):
        return await self.controller.players.operations.add(**operation.model_dump())

    async def get_all_operations_in_session(self, session_id: int):
        return await self.controller.players.operations.get_all_in_session(session_id)

    async def update_operation(
        self, operation_id: int, update_values: "UpdateCashInOutSchema"
    ):

        return await self.controller.players.operations(
            operation_id, **update_values.model_dump(exclude_none=True)
        )

    async def add_credit_deposit_operation(self, operation: "AddCreditDepositSchema"):
        return await self.controller.players.credit_deposits.add(
            **operation.model_dump()
        )

    async def update_credit_deposit_operation(
        self, operation_id: int, update_values: "UpdateCreditDepositSchema"
    ):
        return await self.controller.players.credit_deposits.update(
            operation_id, **update_values.model_dump(exclude_none=True)
        )

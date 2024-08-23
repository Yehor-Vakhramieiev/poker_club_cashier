from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.controllers import PlayerController
    from api.dependencies import PlayerSearchParams
    from api.schemas import (
        AddPlayerSchema,
        UpdatePlayerSchema,
        UpdatePlayerSessionSchema,
        AddPlayerSessionSchema,
        AddCashInOutSchema,
        UpdateCashInOutSchema,
    )


class PlayerService:
    def __init__(self, player_controller: "PlayerController"):
        self.player_controller = player_controller

    async def add_player(self, player_to_add: "AddPlayerSchema"):
        return await self.player_controller.add_player(**player_to_add.model_dump())

    async def get_players(
        self,
        search_params: "PlayerSearchParams",
        limit: int | None = None,
        offset: int | None = None,
    ):
        return await self.player_controller.get_players(
            limit=limit,
            offset=offset,
            **search_params.model_dump(exclude_none=True),
        )

    async def update_player(self, player_id: int, update_values: "UpdatePlayerSchema"):
        await self.player_controller.update_player(
            player_id,
            **update_values.model_dump(exclude_none=True),
        )

    async def add_session(self, session: "AddPlayerSessionSchema"):
        return await self.player_controller.add_session(**session.model_dump())

    async def get_active_sessions(self):
        return await self.player_controller.get_active_sessions()

    async def update_session(
        self, player_id: int, update_values: "UpdatePlayerSessionSchema"
    ):
        await self.player_controller.update_session(
            player_id,
            **update_values.model_dump(exclude_none=True),
        )

    async def add_operation(self, operation: "AddCashInOutSchema"):
        return await self.player_controller.add_operation(**operation.model_dump())

    async def get_all_operations_in_session(self, session_id: int):
        return await self.player_controller.get_all_in_session(session_id)

    async def update_operation(
        self, operation_id: int, update_values: "UpdateCashInOutSchema"
    ):
        return await self.player_controller.update_operation(
            operation_id, **update_values.model_dump(exclude_none=True)
        )

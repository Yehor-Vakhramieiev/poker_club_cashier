from typing import TYPE_CHECKING, Unpack

from core.models import Player, PlayerSession, CashInOut
from core.repositories import (
    PlayerRepository,
    PlayerSessionRepository,
    CashInOutRepository,
)
from core.structures import (
    AddUpdatePlayerValues,
    GetPlayerFilters,
    AddPlayerSessionValues,
    UpdatePlayerSessionValues,
    AddCashInOutValues,
    UpdateCashInOutValues,
)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class PlayerController:
    def __init__(self, db_session: "AsyncSession"):
        self.player_repo = PlayerRepository(db_session)
        self.session_repo = PlayerSessionRepository(db_session)
        self.cash_repo = CashInOutRepository(db_session)

    async def add_player(self, **player_data: Unpack[AddUpdatePlayerValues]) -> Player:
        player_in_db = await self.player_repo.get(**player_data)

        if player_in_db:
            player, *_ = player_in_db
            return player

        player = Player(**player_data)
        return await self.player_repo.add(player)

    async def get_players(
        self,
        limit: int | None = None,
        offset: int | None = None,
        **filters: Unpack[GetPlayerFilters],
    ) -> list[Player]:
        player: list[Player] = await self.player_repo.get(
            limit=limit, offset=offset, **filters
        )
        if not player:
            return []
        return player

    async def update_player(
        self,
        player_id: int,
        **update_values: Unpack[AddUpdatePlayerValues],
    ):
        await self.player_repo.update()
        await self.player_repo.update(player_id, **update_values)

    async def add_session(self, **session_data: Unpack[AddPlayerSessionValues]) -> dict:
        sess = PlayerSession(**session_data)
        async with self.session_repo:
            created_session, first_name, second_name, nickname = (
                await self.session_repo.add(sess)
            )
        return {
            "id": created_session.id,
            "player_id": created_session.player_id,
            "started_at": created_session.started_at,
            "finished_at": created_session.finished_at,
            "win_loss_amount": created_session.win_loss_amount,
            "player_first_name": first_name,
            "player_second_name": second_name,
            "player_nickname": nickname,
        }

    async def get_active_sessions(self) -> list[dict]:
        sessions = await self.session_repo.get_all_active()
        sessions_in_schemas = []
        for session in sessions:
            sess, first_name, second_name, nickname = session
            sessions_in_schemas.append(
                {
                    "player_id": sess.player_id,
                    "started_at": sess.started_at,
                    "finished_at": sess.finished_at,
                    "win_loss_amount": sess.win_loss_amount,
                    "id": sess.id,
                    "player_first_name": first_name,
                    "player_second_name": second_name,
                    "player_nickname": nickname,
                }
            )
        return sessions_in_schemas

    async def update_session(
        self, player_id: int, **update_values: Unpack[UpdatePlayerSessionValues]
    ):
        await self.session_repo.update(player_id, **update_values)

    async def add_operation(self, values: Unpack[AddCashInOutValues]) -> CashInOut:
        operation = CashInOut(**values)
        return await self.cash_repo.add(operation)

    async def get_all_in_session(self, session_id: int) -> list[CashInOut]:
        return await self.cash_repo.get_all_in_session(session_id)

    async def update_operation(
        self, operation_id: int, **update_values: Unpack[UpdateCashInOutValues]
    ):
        await self.cash_repo.update(operation_id, **update_values)

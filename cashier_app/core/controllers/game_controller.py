from typing import TYPE_CHECKING, Unpack

from core.models import GameSession, TableSession
from core.repositories import GameSessionRepository, TableSessionRepository
from core.structures import (
    AddUpdateGameSessionValues,
    AddTableSessionValues,
    UpdateTableSessionValues,
)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class GameController:
    def __init__(self, db_session: "AsyncSession"):
        self.game_session_repo = GameSessionRepository(db_session)
        self.table_session_repo = TableSessionRepository(db_session)

    async def add_game_session(
        self,
        **session_data: Unpack[AddUpdateGameSessionValues],
    ) -> GameSession:
        session = GameSession(**session_data)
        return await self.game_session_repo.add(session)

    async def get_game_sessions(
        self,
        **session_data: Unpack[dict],
    ) -> list[GameSession]: ...

    async def update_game_session(
        self,
        session_id: int,
        **session_data: Unpack[AddUpdateGameSessionValues],
    ) -> None:
        await self.game_session_repo.update(session_id, **session_data)
        return

    async def add_table_session(
        self, **session_data: Unpack[AddTableSessionValues]
    ) -> TableSession:
        session = TableSession(**session_data)
        return await self.table_session_repo.add(session)

    async def update_table_session(
        self,
        session_id: int,
        **session_data: Unpack[UpdateTableSessionValues],
    ) -> None:
        await self.table_session_repo.update(session_id, **session_data)
        return

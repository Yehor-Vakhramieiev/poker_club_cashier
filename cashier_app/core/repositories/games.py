from typing import Unpack

from core.models import GameSession, TableSession, Expense
from core.structures import AddUpdateGameSessionValues, UpdateTableSessionValues
from .base import BaseRepository


class GameSessionRepository(BaseRepository[GameSession]):
    __model__ = GameSession

    # TODO: Implement this method to get all sessions in the database by filters
    async def get(self) -> list[GameSession]:
        return await self._get()

    async def update(
        self, session_id: int, **values: Unpack[AddUpdateGameSessionValues]
    ) -> None:
        return await self._update(session_id, **values)


class TableSessionRepository(BaseRepository[TableSession]):
    __model__ = TableSession

    async def update(
        self, session_id: int, **values: Unpack[UpdateTableSessionValues]
    ) -> None:
        return await self._update(session_id, **values)


class ExpenseRepository(BaseRepository[Expense]):
    __model__ = Expense

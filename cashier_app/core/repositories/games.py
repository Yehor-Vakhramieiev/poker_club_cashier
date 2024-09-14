from typing import Unpack

from core.models import GameSession, TableSession, Expense
from core.structures import (
    AddUpdateGameSessionValues,
    UpdateTableSessionValues,
    AddTableSessionValues,
)
from .base import BaseRepository

__all__ = (
    "GameSessionRepository",
    "TableSessionRepository",
    "ExpenseRepository",
)


class GameSessionRepository(BaseRepository):
    __model__ = GameSession

    # TODO: Implement this method to get all sessions in the database by filters
    async def get(self) -> list[GameSession]:
        return await self._get()

    async def update(
        self, session_id: int, **values: Unpack[AddUpdateGameSessionValues]
    ) -> None:
        return await self._update(session_id, **values)


class TableSessionRepository(BaseRepository):
    __model__ = TableSession

    async def add(self, **values: Unpack[AddTableSessionValues]):
        return await self._add(**values)

    async def update(
        self, session_id: int, **values: Unpack[UpdateTableSessionValues]
    ) -> None:
        return await self._update(session_id, **values)


class ExpenseRepository(BaseRepository):
    __model__ = Expense

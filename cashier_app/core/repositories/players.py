from typing import TYPE_CHECKING, Unpack, override

from sqlalchemy import select

from core.models import PlayerSession, Player, CashInOut
from core.structures import (
    GetPlayerFilters,
    AddUpdatePlayerValues,
    UpdatePlayerSessionValues,
    UpdateCashInOutValues,
)
from .base import BaseRepository

if TYPE_CHECKING:
    ...


class PlayerRepository(BaseRepository[Player]):
    __model__ = Player

    async def get(
        self,
        limit: int | None = None,
        offset: int | None = None,
        **filters: Unpack[GetPlayerFilters],
    ) -> list[Player]:
        return await self._get(limit=limit, offset=offset, **filters)

    async def update(self, pk: int, **values: Unpack[AddUpdatePlayerValues]) -> None:
        return await self._update(pk, **values)


class PlayerSessionRepository(BaseRepository[PlayerSession]):
    __model__ = PlayerSession

    @override
    async def add(self, session: PlayerSession) -> tuple[PlayerSession, str, str, str]:
        session = await super().add(session)
        player = await session.awaitable_attrs.player
        return (
            session,
            player.first_name,
            player.second_name,
            player.nickname,
        )

    async def get_all_active(self) -> list[tuple["PlayerSession", str, str, str]]:
        stmt = (
            select(PlayerSession)
            .where(PlayerSession.finished_at == None)
            .join(Player, PlayerSession.player_id == Player.id)
            .add_columns(Player.first_name, Player.second_name, Player.nickname)
            .order_by(PlayerSession.id)
        )
        result = await self.session.execute(stmt)
        return result.all()  # type: ignore

    async def update(
        self, session_id: int, **values: Unpack[UpdatePlayerSessionValues]
    ) -> None:
        return await self._update(session_id, **values)


class CashInOutRepository(BaseRepository[CashInOut]):
    __model__ = CashInOut

    async def update(
        self,
        operation_id: int,
        **values: Unpack[UpdateCashInOutValues],
    ) -> None:
        return await self._update(operation_id, **values)

    async def get_all_in_session(self, session_id: int) -> list[CashInOut]:
        return await self._get(player_session_id=session_id)

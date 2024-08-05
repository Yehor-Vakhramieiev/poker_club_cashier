import datetime
from typing import TYPE_CHECKING, TypedDict, Unpack

from sqlalchemy import select, update, func

from core.models import Player, PlayerSession
from core.repositories.base import BaseRepository

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from sqlalchemy import Select


class UpdatePlayerValues(TypedDict, total=False):
    first_name: str
    second_name: str
    nickname: str
    birth_date: datetime.date
    phone_number: str
    club_card_number: str


class UpdatePlayerSessionValues(TypedDict, total=False):
    started_at: datetime.datetime
    finished_at: datetime.datetime
    win_loss_amount: int


class SearchPlayerFilters(TypedDict, total=False):
    id: int
    first_name: str
    second_name: str
    nickname: str
    phone_number: str
    club_card_number: str


class PlayerRepository(BaseRepository):
    async def get_player(self, **filters: Unpack[SearchPlayerFilters]) -> Player | None:
        if not filters:
            return None

        stmt = select(Player)

        stmt = self._set_filters_in_stmt(stmt, filters)

        return await self.session.scalar(stmt)

    async def get_players(
        self, limit: int | None = None, offset: int | None = None
    ) -> list[Player]:
        stmt = select(Player).limit(limit).offset(offset)
        result = await self.session.scalars(stmt)
        return result.all()  # type: ignore

    async def add_player(self, player: Player) -> Player:
        player_in_db = await self.get_player(club_card_number=player.club_card_number)

        if player_in_db:
            return player_in_db

        self.session.add(player)
        await self.session.commit()
        await self.session.refresh(player)
        return player

    async def update_player(
        self, player_id: int, **values: Unpack[UpdatePlayerValues]
    ) -> None:
        stmt = update(Player).where(Player.id == player_id).values(**values)
        await self.session.execute(stmt)
        await self.session.commit()
        return

    async def add_session(
        self, session: PlayerSession
    ) -> tuple[PlayerSession, str, str, str]:
        self.session.add(session)
        await self.session.commit()
        await self.session.refresh(session)
        player = await session.awaitable_attrs.player
        return (
            session,
            player.first_name,
            player.second_name,
            player.nickname,
        )

    async def get_active_sessions(
        self, date: datetime.date
    ) -> list[tuple["PlayerSession", str, str, str]]:
        stmt = (
            select(PlayerSession)
            .where(func.DATE(PlayerSession.started_at) == date)
            .where(PlayerSession.finished_at == None)
            .join(Player, PlayerSession.player_id == Player.id)
            .add_columns(Player.first_name, Player.second_name, Player.nickname)
            .order_by(PlayerSession.id)
        )
        result = await self.session.execute(stmt)
        return result.all()  # type: ignore

    async def update_session(
        self, session_id: int, **values: Unpack[UpdatePlayerSessionValues]
    ) -> None:
        stmt = (
            update(PlayerSession).where(PlayerSession.id == session_id).values(**values)
        )
        await self.session.execute(stmt)
        await self.session.commit()
        return

    @staticmethod
    def _set_filters_in_stmt(stmt: "Select", filters: SearchPlayerFilters):
        for field, value in filters.items():
            stmt = stmt.where(getattr(Player, field) == value)
        return stmt

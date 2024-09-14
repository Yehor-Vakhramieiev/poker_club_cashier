from typing import TYPE_CHECKING, Unpack, Literal, overload

from sqlalchemy.orm import joinedload

from core.models import PlayerSession, Player, CashInOut, CreditDeposit
from core.structures import (
    AddUpdatePlayerValues,
    GetPlayerFilters,
    UpdatePlayerSessionValues,
    UpdateCashInOutValues,
    UpdateCreditDepositValues,
    AddPlayerSessionValues,
    AddCashInOutValues,
    AddCreditDepositValues,
)
from .base import BaseRepository

if TYPE_CHECKING:
    ...

__all__ = (
    "PlayerRepository",
    "PlayerSessionRepository",
    "CashInOutRepository",
    "CreditDepositRepository",
)


class PlayerRepository(BaseRepository):
    __model__ = Player

    async def add(self, **values: Unpack[AddUpdatePlayerValues]):
        return await self._add(**values)

    @overload
    async def get(
        self,
        limit: int | None = None,
        offset: int | None = None,
        **filters: Unpack[GetPlayerFilters],
    ) -> list[Player]: ...

    @overload
    async def get(
        self,
        player_id: int,
        details: Literal["all", "sessions", "credits_deposits"] = "all",
    ) -> Player: ...

    async def get(
        self,
        limit: int | None = None,
        offset: int | None = None,
        player_id: int | None = None,
        details: Literal["all", "sessions", "credits_deposits"] = "all",
        **filters: Unpack[GetPlayerFilters],
    ) -> list[Player] | Player:
        options = []
        use_list = True

        if player_id:
            filters["id"] = player_id
            use_list = False

            if details in ["sessions", "credits_deposits"]:
                options += [joinedload(getattr(Player, str(details))).joinedload("*")]
            else:
                options += [
                    joinedload(Player.sessions).joinedload("*"),
                    joinedload(Player.credits_deposits),
                ]

        return await self._get(
            options=options, use_list=use_list, limit=limit, offset=offset, **filters
        )

    async def update(self, pk: int, **values: Unpack[AddUpdatePlayerValues]) -> None:
        return await self._update(pk, **values)


class PlayerSessionRepository(BaseRepository):
    __model__ = PlayerSession

    async def add(self, **values: Unpack[AddPlayerSessionValues]) -> dict:
        session = await self._add(**values)
        player = await session.awaitable_attrs.player
        return dict(
            session.__dict__,
            player_first_name=player.first_name,
            player_second_name=player.second_name,
            player_nickname=player.nickname,
        )

    async def get_all_active(self) -> list[dict]:
        options = (joinedload(PlayerSession.player),)
        result = await self._get(options=options, finished_at=None)

        return [
            dict(
                sess.__dict__,
                player_first_name=sess.player.first_name,
                player_second_name=sess.player.second_name,
                player_nickname=sess.player.nickname,
            )
            for sess in result
        ]

    async def update(
        self, session_id: int, **values: Unpack[UpdatePlayerSessionValues]
    ) -> None:
        return await self._update(session_id, **values)


class CashInOutRepository(BaseRepository):
    __model__ = CashInOut

    async def add(self, **values: Unpack[AddCashInOutValues]) -> CashInOut:
        return await self._add(**values)

    async def update(
        self,
        operation_id: int,
        **values: Unpack[UpdateCashInOutValues],
    ) -> None:
        return await self._update(operation_id, **values)

    async def get_all_in_session(self, session_id: int) -> list[CashInOut]:
        return await self._get(player_session_id=session_id)


class CreditDepositRepository(BaseRepository):
    __model__ = CreditDeposit

    async def add(self, **values: Unpack[AddCreditDepositValues]) -> CreditDeposit:
        return await self._add(**values)

    async def update(
        self, operation_id: int, **values: Unpack[UpdateCreditDepositValues]
    ):
        return await self._update(operation_id, **values)

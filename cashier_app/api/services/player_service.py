import datetime
from typing import TYPE_CHECKING

from api.schemas import (
    AddPlayerSchema,
    PlayerSchema,
    UpdatePlayerSchema,
    PlayerSessionSchema,
    UpdatePlayerSessionSchema,
    AddPlayerSessionSchema,
)
from core.models import Player, PlayerSession

if TYPE_CHECKING:
    from core.repositories import PlayerRepository


class PlayerService:
    def __init__(
        self,
        player_repository: "PlayerRepository",
    ):
        self.player_repository = player_repository

    async def add_player(self, player_to_add: AddPlayerSchema) -> PlayerSchema:
        player: Player = Player(
            first_name=player_to_add.first_name,
            second_name=player_to_add.second_name,
            nickname=player_to_add.nickname,
            birth_date=player_to_add.birth_date,
            phone_number=player_to_add.phone_number,
            club_card_number=player_to_add.club_card_number,
        )
        player: Player = await self.player_repository.add_player(player)
        return PlayerSchema.model_validate(player)

    async def get_player_by_id(self, player_id: int) -> PlayerSchema | None:
        player: Player = await self.player_repository.get_player(id=player_id)
        if not player:
            return None
        return PlayerSchema.model_validate(player)

    async def get_players(
        self,
        limit: int | None = None,
        offset: int | None = None,
    ) -> list[PlayerSchema | None]:
        players: list[Player] = await self.player_repository.get_players(
            limit=limit, offset=offset
        )
        if not players:
            return []

        return [PlayerSchema.model_validate(player_) for player_ in players]

    async def update_player(self, player_id: int, update_values: UpdatePlayerSchema):
        await self.player_repository.update_player(
            player_id, **update_values.model_dump(exclude_none=True)
        )

    async def add_session(
        self, session: AddPlayerSessionSchema
    ) -> "PlayerSessionSchema":
        sess = PlayerSession(
            player_id=session.player_id,
            started_at=session.started_at,
            finished_at=session.finished_at,
            win_loss_amount=session.win_loss_amount,
        )
        created_session, first_name, second_name, nickname = (
            await self.player_repository.add_session(sess)
        )
        session_in_schema = PlayerSessionSchema(
            id=created_session.id,
            player_id=created_session.player_id,
            started_at=created_session.started_at,
            finished_at=created_session.finished_at,
            win_loss_amount=created_session.win_loss_amount,
            player_first_name=first_name,
            player_second_name=second_name,
            player_nickname=nickname,
        )
        return session_in_schema

    async def get_active_sessions(self) -> list[PlayerSessionSchema | None]:
        sessions = await self.player_repository.get_active_sessions(
            datetime.date.today()
        )
        sessions_in_schemas = []
        for session in sessions:
            sess, first_name, second_name, nickname = session
            sessions_in_schemas.append(
                PlayerSessionSchema(
                    player_id=sess.player_id,
                    started_at=sess.started_at,
                    finished_at=sess.finished_at,
                    win_loss_amount=sess.win_loss_amount,
                    id=sess.id,
                    player_first_name=first_name,
                    player_second_name=second_name,
                    player_nickname=nickname,
                )
            )
        return sessions_in_schemas

    async def update_session(
        self, player_id: int, update_values: UpdatePlayerSessionSchema
    ):
        await self.player_repository.update_player(
            player_id, **update_values.model_dump(exclude_none=True)
        )

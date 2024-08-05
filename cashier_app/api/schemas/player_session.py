import datetime

from .base import BaseSchema


class BasePlayerSessionSchema(BaseSchema):
    player_id: int
    started_at: datetime.datetime
    finished_at: datetime.datetime | None = None
    win_loss_amount: int | None = None


class PlayerSessionSchema(BasePlayerSessionSchema):
    id: int
    player_first_name: str | None = None
    player_second_name: str | None = None
    player_nickname: str | None = None


class AddPlayerSessionSchema(BasePlayerSessionSchema): ...


class UpdatePlayerSessionSchema(BaseSchema):
    started_at: datetime.datetime | None = None
    finished_at: datetime.datetime | None = None
    win_loss_amount: int | None = None

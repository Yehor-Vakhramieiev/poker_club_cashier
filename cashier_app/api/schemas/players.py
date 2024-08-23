import datetime

from core.structures import OperationType
from .base import BaseSchema


class BasePlayerSchema(BaseSchema):
    first_name: str
    second_name: str
    nickname: str | None = None
    birth_date: datetime.date | None = None
    phone_number: str | None = None
    club_card_number: str


class PlayerSchema(BasePlayerSchema):
    id: int
    current_credit_deposit: int | None


class AddPlayerSchema(BasePlayerSchema): ...


class UpdatePlayerSchema(BaseSchema):
    first_name: str | None = None
    second_name: str | None = None
    nickname: str | None = None
    birth_date: datetime.date | None = None
    phone_number: str | None = None
    club_card_number: str | None = None


class PlayerDetailSchema(PlayerSchema): ...


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


class BaseCashInOutSchema(BaseSchema):
    type: OperationType
    amount: int
    time: datetime.time
    description: str | None


class CashInOutSchema(BaseCashInOutSchema):
    player_session_id: int


class AddCashInOutSchema(CashInOutSchema): ...


class UpdateCashInOutSchema(BaseSchema):
    type: OperationType | None = None
    amount: int | None = None
    time: datetime.time | None = None
    description: str | None = None

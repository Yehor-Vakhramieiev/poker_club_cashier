import datetime

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

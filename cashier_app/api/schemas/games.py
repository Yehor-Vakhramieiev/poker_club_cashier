import datetime

from .base import BaseSchema

__all__ = (
    "BaseGameSessionSchema",
    "GameSessionSchema",
    "AddGameSessionSchema",
    "UpdateGameSessionSchema",
)


class BaseGameSessionSchema(BaseSchema):
    started_at: datetime.datetime
    finished_at: datetime.datetime
    rake: int


class GameSessionSchema(BaseGameSessionSchema):
    id: int


class AddGameSessionSchema(BaseGameSessionSchema): ...


class UpdateGameSessionSchema(BaseSchema):
    started_at: datetime.datetime | None = None
    finished_at: datetime.datetime | None = None
    rake: int | None = None


class BaseTableSessionSchema(BaseSchema):
    game_session_id: int
    table_number: int
    game_type: str
    started_at: datetime.datetime
    finished_at: datetime.datetime
    rake: int


class TableSessionSchema(BaseTableSessionSchema):
    id: int


class AddTableSessionValues(BaseTableSessionSchema): ...


class UpdateTableSessionSchema(BaseSchema):
    table_number: int | None = None
    game_type: str | None = None
    started_at: datetime.datetime | None = None
    finished_at: datetime.datetime | None = None
    rake: int | None = None


class BaseCashRegisterSchema(BaseSchema):
    amount: int
    date: datetime.datetime


class CashRegisterSchema(BaseCashRegisterSchema): ...


class AddCashRegisterValues(BaseCashRegisterSchema): ...


class UpdateCashRegisterSchema(BaseSchema):
    amount: int | None = None


class ChipsSchema(BaseSchema):
    one: int | None = None
    five: int | None = None
    twenty_five: int | None = None
    hundred: int | None = None
    five_hundred: int | None = None
    thousand: int | None = None
    five_thousand: int | None = None
    twenty_five_thousand: int | None = None

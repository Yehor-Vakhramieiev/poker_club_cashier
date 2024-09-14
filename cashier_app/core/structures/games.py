import datetime
from typing import TypedDict

__all__ = (
    "AddUpdateGameSessionValues",
    "UpdateTableSessionValues",
    "AddTableSessionValues",
    "UpdateCashRegisterValues",
    "AddCashRegisterValues",
    "AddUpdateChipsValues",
)


class AddUpdateGameSessionValues(TypedDict, total=False):
    started_at: datetime.datetime
    finished_at: datetime.datetime
    rake: int


class UpdateTableSessionValues(TypedDict, total=False):
    table_number: int
    game_type: str
    started_at: datetime.datetime
    finished_at: datetime.datetime
    rake: int


class AddTableSessionValues(UpdateTableSessionValues):
    game_session_id: int


class UpdateCashRegisterValues(TypedDict, total=False):
    amount: int


class AddCashRegisterValues(UpdateCashRegisterValues):
    date: datetime.datetime


class AddUpdateChipsValues(TypedDict, total=False):
    one: int
    five: int
    twenty_five: int
    hundred: int
    five_hundred: int
    thousand: int
    five_thousand: int
    twenty_five_thousand: int

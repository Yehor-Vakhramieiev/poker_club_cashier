import datetime
from enum import Enum
from typing import TypedDict, Literal

__all__ = (
    "CreditDepositType",
    "CreditDepositType",
    "OperationType",
    "AddUpdatePlayerValues",
    "GetPlayerFilters",
    "UpdatePlayerSessionValues",
    "AddPlayerSessionValues",
    "UpdateCashInOutValues",
    "AddCashInOutValues",
    "UpdateCreditDepositValues",
    "AddCreditDepositValues",
)


class CreditDepositType(Enum):
    credit = "credit"
    deposit = "deposit"


class OperationType(Enum):
    cash_in = "cash_in"
    cash_out = "cash_out"


class AddUpdatePlayerValues(TypedDict, total=False):
    first_name: str
    second_name: str
    nickname: str
    birth_date: datetime.date
    phone_number: str
    club_card_number: str


class GetPlayerFilters(TypedDict, total=False):
    id: int
    first_name: str
    second_name: str
    nickname: str
    phone_number: str
    club_card_number: str


class UpdatePlayerSessionValues(TypedDict, total=False):
    started_at: datetime.datetime
    finished_at: datetime.datetime
    win_loss_amount: int


class AddPlayerSessionValues(UpdatePlayerSessionValues):
    player_id: int


class UpdateCashInOutValues(TypedDict, total=False):
    type: Literal["cash_in", "cash_out"]
    amount: int
    time: datetime.time
    description: str


class AddCashInOutValues(UpdateCashInOutValues):
    player_session_id: int


class UpdateCreditDepositValues(TypedDict, total=False):
    given_at: datetime.datetime
    operation_type: Literal["credit", "deposit"]
    amount: int


class AddCreditDepositValues(UpdateCreditDepositValues):
    player_id: int

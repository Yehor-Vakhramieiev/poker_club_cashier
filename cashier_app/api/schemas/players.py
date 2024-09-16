import datetime

from core.structures import OperationType, CreditDepositType
from .base import BaseSchema

__all__ = (
    "BasePlayerSchema",
    "PlayerSchema",
    "AddPlayerSchema",
    "UpdatePlayerSchema",
    "PlayerDetailSchema",
    "BasePlayerSessionSchema",
    "PlayerSessionSchema",
    "AddPlayerSessionSchema",
    "UpdatePlayerSessionSchema",
    "PlayerSessionDetailSchema",
    "BaseCashInOutSchema",
    "CashInOutSchema",
    "AddCashInOutSchema",
    "UpdateCashInOutSchema",
    "BaseCreditDepositSchema",
    "CreditDepositSchema",
    "AddCreditDepositSchema",
    "UpdateCreditDepositSchema",
)


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


class PlayerShortSchema(BaseSchema):
    first_name: str | None
    second_name: str | None
    nickname: str | None


class PlayerDetailSchema(PlayerSchema):
    sessions: list["PlayerSessionDetailSchema"] | list[None]
    credits_deposits: list["CreditDepositSchema"] | list[None]


class BasePlayerSessionSchema(BaseSchema):
    player_id: int
    started_at: datetime.datetime
    finished_at: datetime.datetime | None = None
    win_loss_amount: int | None = None


class PlayerSessionSchema(BasePlayerSessionSchema):
    id: int
    player: PlayerShortSchema
    # player_first_name: str | None = None
    # player_second_name: str | None = None
    # player_nickname: str | None = None


class PlayerSessionDetailSchema(PlayerSessionSchema):
    cash_in_outs: list["CashInOutSchema"] | list[None]


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


class BaseCreditDepositSchema(BaseSchema):
    given_at: datetime.datetime
    operation_type: CreditDepositType
    amount: int


class CreditDepositSchema(BaseCreditDepositSchema):
    player_id: int


class AddCreditDepositSchema(CreditDepositSchema): ...


class UpdateCreditDepositSchema(BaseSchema):
    given_at: datetime.datetime | None = None
    operation_type: CreditDepositType | None = None
    amount: int | None = None

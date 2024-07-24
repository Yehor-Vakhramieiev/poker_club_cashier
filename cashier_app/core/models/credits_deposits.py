from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base

if TYPE_CHECKING:
    from core.models import Player


class OperationType(Enum):
    credit = "credit"
    deposit = "deposit"


class CreditDeposit(Base):
    __tablename__ = "credits_deposits"

    player_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("players.id"),
        nullable=False,
    )
    given_at: Mapped[datetime]
    operation_type: Mapped[OperationType]
    amount: Mapped[int]

    player: Mapped["Player"] = relationship(
        "Player",
        back_populates="credits_deposits",
        uselist=False,
    )

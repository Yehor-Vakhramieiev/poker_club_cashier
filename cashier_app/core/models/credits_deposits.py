import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.structures import CreditDepositType

if TYPE_CHECKING:
    from core.models import Player


class CreditDeposit(Base):
    __tablename__ = "credits_deposits"

    player_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("players.id"),
        nullable=False,
    )
    given_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    operation_type: Mapped[CreditDepositType]
    amount: Mapped[int]

    player: Mapped["Player"] = relationship(
        "Player",
        back_populates="credits_deposits",
        uselist=False,
    )

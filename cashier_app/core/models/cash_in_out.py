from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base

if TYPE_CHECKING:
    from .player_session import PlayerSession


class OperationType(Enum):
    cash_in = "cash_in"
    cash_out = "cash_out"


class CashInOut(Base):
    __tablename__ = "cash_in_outs"

    player_session_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("player_sessions.id"),
    )
    type: Mapped[OperationType]
    amount: Mapped[int]
    description: Mapped[str]

    player_session: Mapped["PlayerSession"] = relationship(
        "PlayerSession",
        back_populates="cash_in_outs",
        uselist=False,
    )

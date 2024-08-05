import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from core.models import Player
    from .cash_in_out import CashInOut


class PlayerSession(Base):
    __tablename__ = "player_sessions"

    player_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("players.id"), nullable=False
    )
    started_at: Mapped[datetime.datetime | None] = mapped_column(DateTime(timezone=True))
    finished_at: Mapped[datetime.datetime | None] = mapped_column(DateTime(timezone=True))
    win_loss_amount: Mapped[int | None]

    player: Mapped["Player"] = relationship("Player", back_populates="sessions")
    cash_in_outs: Mapped[list["CashInOut"]] = relationship(
        "CashInOut",
        back_populates="player_session",
        uselist=True,
    )

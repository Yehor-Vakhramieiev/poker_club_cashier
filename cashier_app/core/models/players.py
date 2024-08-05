import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .base import Base

if TYPE_CHECKING:
    from .player_session import PlayerSession
    from .credits_deposits import CreditDeposit


class Player(Base):
    __tablename__ = "players"

    first_name: Mapped[str]
    second_name: Mapped[str]
    nickname: Mapped[str | None]
    birth_date: Mapped[datetime.date | None]
    phone_number: Mapped[str | None]
    club_card_number: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    current_credit_deposit: Mapped[int | None]

    sessions: Mapped[list["PlayerSession"]] = relationship(
        "PlayerSession",
        back_populates="player",
        uselist=True,
    )
    credits_deposits: Mapped[list["CreditDeposit"]] = relationship(
        "CreditDeposit",
        back_populates="player",
        uselist=True,
    )

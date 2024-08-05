import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, relationship, mapped_column

from core.models import Base

if TYPE_CHECKING:
    from .table_session import TableSession


class GameSession(Base):
    __tablename__ = "game_sessions"

    started_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    finished_at: Mapped[datetime.datetime | None] = mapped_column(DateTime(timezone=True))
    rake: Mapped[int | None]

    table_sessions: Mapped[list["TableSession"]] = relationship(
        "TableSession",
        back_populates="game_session",
        uselist=True,
    )

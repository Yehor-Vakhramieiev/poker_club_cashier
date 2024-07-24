from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base

if TYPE_CHECKING:
    from .game_session import GameSession


class TableSession(Base):
    __tablename__ = "table_sessions"

    game_session_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("game_sessions.id")
    )
    table_number: Mapped[int]
    game_type: Mapped[str]
    started_at: Mapped[datetime]
    finished_at: Mapped[datetime | None]
    rake: Mapped[int | None]

    game_session: Mapped["GameSession"] = relationship(
        "GameSession",
        back_populates="table_sessions",
        uselist=False,
    )

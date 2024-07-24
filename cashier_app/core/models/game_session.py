from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from core.models import Base

if TYPE_CHECKING:
    from .table_session import TableSession


class GameSession(Base):
    __tablename__ = "game_sessions"

    started_at: Mapped[datetime]
    finished_at: Mapped[datetime | None]
    rake: Mapped[int | None]

    table_sessions: Mapped[list["TableSession"]] = relationship(
        "TableSession",
        back_populates="game_session",
        uselist=True,
    )

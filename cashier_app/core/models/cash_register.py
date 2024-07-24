from datetime import datetime

from sqlalchemy.orm import Mapped

from core.models import Base


class CashRegister(Base):
    __tablename__ = "cash_register"

    date: Mapped[datetime]
    amount: Mapped[int]

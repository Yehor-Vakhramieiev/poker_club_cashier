from sqlalchemy.orm import Mapped

from core.models import Base


class ChipQuantity(Base):
    __tablename__ = "chips_quantity"

    one: Mapped[int]
    five: Mapped[int]
    twenty_five: Mapped[int]
    hundred: Mapped[int]
    five_hundred: Mapped[int]
    thousand: Mapped[int]
    five_thousand: Mapped[int]
    twenty_five_thousand: Mapped[int]

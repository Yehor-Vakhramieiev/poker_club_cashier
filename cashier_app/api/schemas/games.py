import datetime

from .base import BaseSchema


class BaseGameSessionSchema(BaseSchema):
    started_at: datetime.datetime
    finished_at: datetime.datetime | None = None
    rake: int | None = None


class GameSessionSchema(BaseGameSessionSchema):
    id: int

class AddGameSessionSchema(BaseGameSessionSchema): ...


class UpdateGameSessionSchema(BaseGameSessionSchema):
    started_at: datetime.datetime | None = None
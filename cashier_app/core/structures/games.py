import datetime
from typing import TypedDict


class AddUpdateGameSessionValues(TypedDict, total=False):
    started_at: datetime.datetime
    finished_at: datetime.datetime
    rake: int


class UpdateTableSessionValues(TypedDict, total=False):
    table_number: int
    game_type: str
    started_at: datetime.datetime
    finished_at: datetime.datetime
    rake: int


class AddTableSessionValues(UpdateTableSessionValues):
    game_session_id: int

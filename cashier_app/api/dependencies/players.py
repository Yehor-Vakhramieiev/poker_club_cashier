from pydantic import BaseModel


class PlayerSearchParams(BaseModel):
    id: int | None = None
    first_name: str | None = None
    second_name: str | None = None
    nickname: str | None = None
    phone_number: str | None = None
    club_card_number: str | None = None

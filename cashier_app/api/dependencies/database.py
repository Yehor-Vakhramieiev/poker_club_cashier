from typing import TYPE_CHECKING, Annotated, AsyncGenerator

from fastapi import Depends

from api.services import PlayerService
from core.database import pg_db_helper
from core.repositories import PlayerRepository

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_player_repository(
    session: Annotated["AsyncSession", Depends(pg_db_helper.session_getter)]
) -> AsyncGenerator[PlayerRepository, None]:
    yield PlayerRepository(session)


async def get_player_service(
    player_repository: Annotated[PlayerRepository, Depends(get_player_repository)],
) -> AsyncGenerator[PlayerService, None]:
    yield PlayerService(player_repository)

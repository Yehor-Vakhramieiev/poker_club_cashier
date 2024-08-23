from typing import TYPE_CHECKING, Annotated, AsyncGenerator

from fastapi import Depends

from api.services import PlayerService
from core.database import pg_db_helper
from core.controllers import PlayerController

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_player_controller(
    session: Annotated["AsyncSession", Depends(pg_db_helper.session_getter)]
) -> AsyncGenerator[PlayerController, None]:
    yield PlayerController(session)


async def get_player_service(
    player_controller: Annotated[PlayerController, Depends(get_player_controller)],
) -> AsyncGenerator[PlayerService, None]:
    yield PlayerService(player_controller)

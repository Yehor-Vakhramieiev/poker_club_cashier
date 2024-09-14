from typing import TYPE_CHECKING, Annotated, AsyncGenerator

from fastapi import Depends

from api.services import PlayerService
from core.controllers import Controller
from core.database import pg_db_helper

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_player_controller(
    session: Annotated["AsyncSession", Depends(pg_db_helper.session_getter)]
) -> AsyncGenerator[Controller, None]:
    yield Controller(session)


async def get_player_service(
    player_controller: Annotated[Controller, Depends(get_player_controller)],
) -> AsyncGenerator[PlayerService, None]:
    yield PlayerService(player_controller)

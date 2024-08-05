from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.repositories import PlayerRepository


class PlayerController:
    def __init__(self, player_repository: "PlayerRepository"):
        self.player_repository = player_repository

    async def add_player[CT, RT](self, player: CT) -> RT: ...

from typing import TYPE_CHECKING

from core.repositories import (
    PlayerRepository,
    PlayerSessionRepository,
    CashInOutRepository,
    CreditDepositRepository,
)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class Controller:
    class _PlayerControllers:
        def __init__(self, session: "AsyncSession"):
            self.__session = session

        @property
        def controller(self):
            return PlayerRepository(self.__session)

        @property
        def sessions(self):
            return PlayerSessionRepository(self.__session)

        @property
        def operations(self):
            return CashInOutRepository(self.__session)

        @property
        def credit_deposits(self):
            return CreditDepositRepository(self.__session)

    class _GameControllers:
        def __init__(self, session: "AsyncSession"):
            self.__session = session

        @property
        def controller(self):
            return PlayerRepository(self.__session)

        @property
        def sessions(self):
            return PlayerSessionRepository(self.__session)

        @property
        def operations(self):
            return CashInOutRepository(self.__session)

        @property
        def credit_deposits(self):
            return CreditDepositRepository(self.__session)

    def __init__(self, db_session: "AsyncSession"):
        self.__session = db_session

    @property
    def players(self):
        return self._PlayerControllers(self.__session)

    @property
    def games(self):
        return self._GameControllers(self.__session)

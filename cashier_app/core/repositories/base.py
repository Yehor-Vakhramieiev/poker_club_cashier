from typing import TYPE_CHECKING

from sqlalchemy import select, update

from .meta import RepoMeta

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from core.models import Base


class BaseRepository(metaclass=RepoMeta):
    __model__: type["Base"]

    def __init__(self, session: "AsyncSession"):
        self.session: "AsyncSession" = session

    async def _get(
        self, /, options=None, use_list=True, limit=None, offset=None, **filters
    ):

        _filters = [
            getattr(self.__model__, field) == value for field, value in filters.items()
        ]

        stmt = (
            select(self.__model__)
            .options(*options)
            .where(*_filters)
            .limit(limit)
            .offset(offset)
            .order_by(self.__model__.id)
        )

        result = await self.session.scalars(stmt)

        if options:
            result = result.unique()

        return result.all() if use_list else result.first()

    async def _add(self, **values):
        instance = self.__model__(**values)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def _update(self, pk, **values):
        stmt = update(self.__model__).where(self.__model__.id == pk).values(**values)  # type: ignore
        await self.session.execute(stmt)
        await self.session.commit()
        return

    async def __aenter__(self):
        return self.session.begin()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"AEXIT {exc_type=}")
        await self.session.rollback()

from typing import TYPE_CHECKING, overload

from sqlalchemy import select, update

from core.models import Base
from .meta import RepoMeta

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository[M: Base](metaclass=RepoMeta):
    __model__: type[M]

    def __init__(self, session: "AsyncSession"):
        self.session: "AsyncSession" = session

    @overload
    async def _get(
        self,
        /,
        limit: int | None = None,
        offset: int | None = None,
        **filters,
    ) -> list[M]:
        _filters = [
            getattr(self.__model__, field) == value for field, value in filters.items()
        ]
        stmt = (
            select(self.__model__)
            .where(*_filters)
            .limit(limit)
            .offset(offset)
            .order_by(self.__model__.id)
        )

        result = await self.session.scalars(stmt)
        return result.all()  # type: ignore

    async def _get(self, *_, **__) -> list[M]:
        stmt = select(self.__model__).order_by(self.__model__.id)
        result = await self.session.scalars(stmt)
        return result.all()  # type: ignore

    async def add(self, instance: M) -> M:
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    # TODO: add type annotation to values with Unpack[] when it will be supported
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

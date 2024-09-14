import inspect

from sqlalchemy.exc import IntegrityError, SQLAlchemyError


def decorator(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)

        except IntegrityError as e:
            print(f"SQLAlchemy Error: {e}")
            raise ZeroDivisionError

        except SQLAlchemyError as e:
            print(f"SQLAlchemy Error: {e}")
            raise ZeroDivisionError

    return wrapper


class RepoMeta(type):
    def __new__(cls, name, bases, dct):
        print("META")
        for key, value in dct.items():
            if inspect.iscoroutinefunction(value) and not key.startswith("_"):
                dct[key] = decorator(value)

        return super().__new__(cls, name, bases, dct)

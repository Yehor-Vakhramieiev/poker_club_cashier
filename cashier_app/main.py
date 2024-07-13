from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core.database import pg_db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await pg_db_helper.dispose()


main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

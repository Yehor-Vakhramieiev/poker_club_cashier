from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import ORJSONResponse

from api import router as api_router
from core.database import pg_db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await pg_db_helper.dispose()


app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

app.include_router(api_router)


@app.exception_handler(ZeroDivisionError)
async def zero_div(request, ex: ZeroDivisionError):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="localhost", port=8000)

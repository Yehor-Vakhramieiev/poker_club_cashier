from fastapi import APIRouter


router = APIRouter(prefix="/tables")


@router.get("")
async def get_table_sessions(): ...


@router.post("")
async def add_table_session(): ...


@router.patch("")
async def update_table_session(): ...

from fastapi import APIRouter


router = APIRouter(prefix="/expenses")


@router.get("")
async def get_expenses_record(): ...


@router.post("")
async def add_expenses_record(): ...


@router.patch("")
async def update_expenses_record(): ...

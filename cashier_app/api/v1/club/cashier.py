from fastapi import APIRouter


router = APIRouter(prefix="/cashier")


@router.get("")
async def get_cash_record(): ...


@router.post("")
async def add_cash_record(): ...


@router.patch("")
async def update_cash_record(): ...

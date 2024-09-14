from typing import TYPE_CHECKING

from fastapi import APIRouter

if TYPE_CHECKING:
    pass

router = APIRouter(prefix="/credit_deposit")


@router.get("")
async def get_credit_deposit(): ...


@router.post("")
async def add_credit_deposit(): ...


@router.patch("")
async def update_credit_deposit(): ...

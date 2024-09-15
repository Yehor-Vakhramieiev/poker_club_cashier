from fastapi import APIRouter


router = APIRouter(prefix="/chips")


@router.get("")
async def get_chips_record(): ...


@router.post("")
async def add_chips_record(): ...

from fastapi import APIRouter


router = APIRouter(prefix="/calculations")


@router.get("/cash")
async def get_cash(): ...

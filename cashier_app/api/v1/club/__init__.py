from fastapi import APIRouter

from .cashier import router as cashier_router
from .chips import router as chips_router
from .expenses import router as expenses_router

router = APIRouter(prefix="/club")

router.include_router(chips_router)
router.include_router(cashier_router)
router.include_router(expenses_router)

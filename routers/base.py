from fastapi import APIRouter
from routers.router_signup import router as router_signup
from routers.router_login import router as router_login


router = APIRouter()

router.include_router(router_signup)
router.include_router(router_login)

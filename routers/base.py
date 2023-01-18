from fastapi import APIRouter

from routers.router_signup import router as router_signup
from routers.router_login import router as router_login
from routers.router_links import router as router_links


router = APIRouter()

router.include_router(router_signup)
router.include_router(router_login)
router.include_router(router_links)

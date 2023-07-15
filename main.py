import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from core.cors import origins
from routers.base import router


def start_application():
    application: FastAPI = FastAPI(title=settings.PROJECT_NAME,
                                   version=settings.PROJECT_VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    application.include_router(router)
    return application


app = start_application()

if __name__ == "__main__":
    is_reload = True if settings.ENVIRONMENT == "development" else False
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=is_reload)

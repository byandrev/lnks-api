import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from core.config import settings
from core.cors import origins
from db.serializers.serializer import serializeDict
from routers.base import router
from schemas.custom_exception import CustomException


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
    
    @application.exception_handler(CustomException)
    async def http_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(status_code=exc.response.status, content=exc.response.dict())
    
    return application


app = start_application()

if __name__ == "__main__":
    is_reload = True if settings.ENVIRONMENT == "development" else False
    uvicorn.run("main:app", host="0.0.0.0", port=settings.PORT, reload=is_reload)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from core.cors import origins
from routers.base import router


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(router)
    return app


app = start_application()


@app.on_event("startup")
async def app_startup():
    # start_client_db(app)
    pass


@app.on_event("shutdown")
def shutdown_db_client():
    # app.mongodb_client.close()
    pass


# if __name__ == "__main__":
#    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

import fastapi
import uvicorn
from fastapi import FastAPI

from app import settings
from app.router.endpoint import api_router


def create_app() -> fastapi.FastAPI:
    app_instance = FastAPI(
        title=settings.project_name,
        version=settings.version,
        openapi_url=f"{settings.api_prefix}/openapi.json",
        debug=settings.debug,
    )

    app_instance.include_router(api_router, prefix=settings.api_prefix)
    return app_instance


app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)

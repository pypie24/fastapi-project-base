from fastapi import APIRouter

from app.sample.api import router as sample_router

api_router = APIRouter()

api_router.include_router(sample_router, prefix="/sample", tags=["samples"])

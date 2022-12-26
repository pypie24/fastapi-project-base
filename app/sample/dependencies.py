from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.sample.crud import SampleCRUD


async def get_sample_crud(
    session: AsyncSession = Depends(get_async_session),
) -> SampleCRUD:
    return SampleCRUD(session=session)

from typing import Optional
from uuid import UUID

from fastapi import HTTPException
from fastapi import status as http_status
from sqlalchemy import delete, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.utils import unpack_row
from app.sample.models import Sample
from app.sample.schemas import SampleCreate, SampleUpdate


class SampleCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: SampleCreate) -> Sample:
        value = data.dict()
        instance = Sample(**value)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get_all(self) -> list[Sample]:
        statement = select(Sample).order_by(Sample.id)
        result = await self.session.execute(statement=statement)
        instances = result.fetchall()  # type: list[Sample] | None
        instances = unpack_row(instances, Sample.__name__)
        return instances

    async def get(self, sample_id: UUID) -> Optional[Sample]:
        statement = select(Sample).where(
            Sample.id == sample_id,
        )
        result = await self.session.execute(statement=statement)
        instance = result.scalar_one_or_none()  # type: Sample | None
        if not instance:
            raise HTTPException(
                status_code=http_status.HTTP_404_NOT_FOUND,
                detail="The sample hasn't been found!",
            )
        return instance

    async def update(self, sample_id: UUID, data: SampleUpdate) -> Sample:
        instance = await self.get(sample_id)  # type: Sample | None
        values = data.dict()
        instance = instance.update(values)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def delete(self, sample_id: UUID) -> bool:
        statement = delete(Sample).where(Sample.id == sample_id)
        await self.session.execute(statement=statement)
        await self.session.commit()
        return True

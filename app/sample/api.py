import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi import status as http_status

from app.sample.crud import SampleCRUD
from app.sample.dependencies import get_sample_crud
from app.sample.models import Sample
from app.sample.schemas import SampleCreate, SampleRead, SampleUpdate

logger = logging.getLogger("uvicorn.access")

router = APIRouter()


@router.get(
    "",
    response_model=list[SampleRead],
    status_code=http_status.HTTP_200_OK,
)
async def get_all(
    model_crud: SampleCRUD = Depends(get_sample_crud),
) -> list[Sample]:

    sample = await model_crud.get_all()
    return sample


@router.get(
    "/{sample_id}",
    response_model=SampleRead,
    status_code=http_status.HTTP_200_OK,
)
async def get(
    sample_id: UUID,
    model_crud: SampleCRUD = Depends(get_sample_crud),
) -> Sample:

    sample = await model_crud.get(sample_id=sample_id)
    return sample


@router.post("", response_model=SampleRead, status_code=http_status.HTTP_200_OK)
async def create(
    data: SampleCreate,
    model_crud: SampleCRUD = Depends(get_sample_crud),
) -> Sample:
    sample = await model_crud.create(data=data)

    return sample


@router.patch(
    "/{sample_id}",
    response_model=SampleRead,
    status_code=http_status.HTTP_200_OK,
)
async def update(
    sample_id: UUID,
    data: SampleUpdate,
    model_crud: SampleCRUD = Depends(get_sample_crud),
) -> Sample:

    sample = await model_crud.update(sample_id=sample_id, data=data)

    return sample


@router.delete(
    "/{sample_id}",
    response_model=bool,
    status_code=http_status.HTTP_200_OK,
)
async def delete(
    sample_id: UUID,
    model_crud: SampleCRUD = Depends(get_sample_crud),
) -> Sample:

    sample = await model_crud.delete(sample_id=sample_id)
    return sample

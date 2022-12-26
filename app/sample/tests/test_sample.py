import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.sample.models import Sample


@pytest.mark.asyncio
async def test_create_sample(
    async_client: AsyncClient,
    async_session: AsyncSession,
    test_data: dict,
    sample_factory,
):
    _ = sample_factory.create()
    payload = test_data["create"]
    response = await async_client.post(
        "/sample",
        json=payload,
    )

    assert response.status_code == 200

    statement = select(Sample)
    results = await async_session.execute(statement=statement)
    results = results.fetchall()
    assert len(results) == 2

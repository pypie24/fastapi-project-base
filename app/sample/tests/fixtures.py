import factory
import pytest
from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy.ext.asyncio import AsyncSession

from app.sample.models import Sample


@pytest.fixture
def sample_factory(async_session: AsyncSession):
    class SampleFactory(SQLAlchemyModelFactory):
        class Meta:
            model = Sample
            sqlalchemy_session = async_session

        message = factory.Faker("first_name")
        active = factory.Faker("random_element", elements=(True, False))

    return SampleFactory


@pytest.fixture
def samples(sample_factory):
    sample_factory.create_batch(4)

import sys

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from app import settings


def get_db_connection_str() -> str:
    db_connection_str = settings.db_async_connection_str

    if "pytest" in sys.modules:
        db_connection_str = settings.db_async_test_connection_str
    return db_connection_str


def create_db_engine(db_connection_str, echo=True, future=True):
    return create_async_engine(db_connection_str, echo=echo, future=future)


db_connection_str = get_db_connection_str()
async_engine = create_async_engine(db_connection_str)


async def get_async_session() -> AsyncSession:
    async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session

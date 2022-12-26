from typing import Optional

from sqlmodel import Field

from app.core.models import TimestampModel, UUIDModel


class Sample(UUIDModel, TimestampModel, table=True):
    __tablename__ = "sample"

    message: Optional[str]
    active: bool = Field(nullable=False)

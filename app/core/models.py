import uuid as uuid_pkg
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import text
from sqlmodel import Field, SQLModel


class HealthCheck(BaseModel):
    name: str
    version: str


class StatusMessage(BaseModel):
    status: bool
    message: str


class UUIDModel(SQLModel):
    id: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )

    def update(self, values):
        for key, value in values.items():
            setattr(self, key, value)
        return self


class TimestampModel(SQLModel):
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={"server_default": text("current_timestamp(0)")},
    )

    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "server_default": text("current_timestamp(0)"),
            "onupdate": text("current_timestamp(0)"),
        },
    )

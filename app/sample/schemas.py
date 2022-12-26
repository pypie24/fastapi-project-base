from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class SampleBase(BaseModel):
    message: Optional[str]
    active: bool

    class Config:
        orm_mode = True


class SampleRead(SampleBase):

    id: UUID
    created_at: datetime
    updated_at: datetime


class SampleUpdate(SampleBase):

    active: Optional[bool]

    class Config:
        orm_mode = True


class SampleCreate(SampleBase):
    class Config:
        orm_mode = True

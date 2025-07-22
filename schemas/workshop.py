from pydantic import BaseModel
from uuid import UUID
from datetime import datetime, timedelta
from typing import Optional

class WorkshopBase(BaseModel):
    title: str
    category: Optional[str] = None
    address: Optional[str] = None
    description: Optional[str] = None
    capacity: Optional[int] = None
    start_date: datetime
    end_date: datetime
    teacher_uuid: UUID

class WorkshopCreate(WorkshopBase):
    pass

class WorkshopRead(WorkshopBase):
    uuid: UUID
    duration: Optional[timedelta]

    class Config:
        orm_mode = True

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from models.frequency import AttendanceStatus
from typing import Optional

class FrequencyBase(BaseModel):
    student_uuid: UUID
    lesson_uuid: UUID
    status: AttendanceStatus

class FrequencyUpdate(BaseModel):
    student_uuid: Optional[UUID] = None
    lesson_uuid: Optional[UUID] = None
    status: Optional[AttendanceStatus] = None

class FrequencyCreate(FrequencyBase):
    pass

class FrequencyRead(FrequencyBase):
    uuid: UUID
    recorded_at: datetime

    class Config:
        orm_mode = True

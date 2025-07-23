from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from models.frequency import AttendanceStatus

class FrequencyBase(BaseModel):
    student_uuid: UUID
    lesson_uuid: UUID
    status: AttendanceStatus

class FrequencyCreate(FrequencyBase):
    pass

class FrequencyRead(FrequencyBase):
    uuid: UUID
    recorded_at: datetime

    class Config:
        orm_mode = True

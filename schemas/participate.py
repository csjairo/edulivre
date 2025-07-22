from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class ParticipateBase(BaseModel):
    student_uuid: UUID
    workshop_uuid: UUID

class ParticipateCreate(ParticipateBase):
    pass

class ParticipateRead(ParticipateBase):
    uuid: UUID
    enrolled_at: datetime

    class Config:
        orm_mode = True

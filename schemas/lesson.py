from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class LessonBase(BaseModel):
    title: str
    description: Optional[str] = None
    class_type: Optional[str] = None
    status: Optional[str] = None
    recording_url: Optional[str] = None
    teacher_uuid: UUID
    workshop_uuid: UUID

class LessonCreate(LessonBase):
    pass

class LessonRead(LessonBase):
    uuid: UUID

    class Config:
        orm_mode = True

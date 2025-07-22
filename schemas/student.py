from pydantic import BaseModel
from uuid import UUID
from models.student import GradeLevel

class StudentBase(BaseModel):
    grade_level: GradeLevel
    interests: str | None = None

class StudentCreate(StudentBase):
    uuid: UUID

class StudentRead(StudentBase):
    uuid: UUID

    class Config:
        orm_mode = True

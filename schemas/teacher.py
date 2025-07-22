from pydantic import BaseModel
from uuid import UUID

class TeacherBase(BaseModel):
    degree: str
    specialties: str

class TeacherCreate(TeacherBase):
    user_uuid: UUID

class TeacherRead(TeacherBase):
    id: int
    user_uuid: UUID

    class Config:
        orm_mode = True

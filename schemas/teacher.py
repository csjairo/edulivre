from pydantic import BaseModel
from uuid import UUID

class TeacherBase(BaseModel):
    degree: str
    specialties: str

class TeacherCreate(TeacherBase):
    uuid: UUID

class TeacherRead(TeacherBase):
    uuid: UUID

    class Config:
        orm_mode = True

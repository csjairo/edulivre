from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class HistoryBase(BaseModel):
    user_uuid: UUID
    action: str

class HistoryCreate(HistoryBase):
    pass

class HistoryRead(HistoryBase):
    uuid: UUID
    created_at: datetime

    class Config:
        orm_mode = True

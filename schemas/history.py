from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class HistoryBase(BaseModel):
    user_uuid: UUID
    action: str

class HistoryCreate(HistoryBase):
    pass

class HistoryUpdate(BaseModel):
    user_uuid: Optional[UUID] = None
    action: Optional[str] = None

class HistoryRead(HistoryBase):
    uuid: UUID
    created_at: datetime

    class Config:
        orm_mode = True

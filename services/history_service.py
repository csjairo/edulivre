from sqlalchemy.orm import Session
from models.history import History
from schemas.history import HistoryCreate
from uuid import UUID

def create_history(db: Session, history_data: HistoryCreate) -> History:
    new_history = History(**history_data.model_dump())
    db.add(new_history)
    db.commit()
    db.refresh(new_history)
    return new_history

def get_history_by_user(db: Session, user_uuid: UUID):
    return db.query(History).filter(History.user_uuid == user_uuid).all()

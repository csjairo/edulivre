from sqlalchemy.orm import Session
from models.history import History
from schemas.history import HistoryCreate
from uuid import UUID
from typing import Optional, Dict, Any

def create_history(db: Session, history_data: HistoryCreate) -> History:
    new_history = History(**history_data.model_dump())
    db.add(new_history)
    db.commit()
    db.refresh(new_history)
    return new_history

def get_history_by_user(db: Session, user_uuid: UUID):
    return db.query(History).filter(History.user_uuid == user_uuid).all()

def get_history_by_id(db: Session, history_uuid: UUID) -> Optional[History]:
    return db.query(History).filter(History.uuid == history_uuid).first()

def update_history(db: Session, history_uuid: UUID, updates: Dict[str, Any]) -> Optional[History]:
    db_history = db.query(History).filter(History.uuid == history_uuid).first()
    if db_history:
        for key, value in updates.items():
            setattr(db_history, key, value)
        db.commit()
        db.refresh(db_history)
    return db_history

def delete_history(db: Session, history_uuid: UUID) -> bool:
    db_history = db.query(History).filter(History.uuid == history_uuid).first()
    if db_history:
        db.delete(db_history)
        db.commit()
        return True
    return False

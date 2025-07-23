from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.history import HistoryCreate, HistoryRead
from services.history_service import create_history, get_history_by_user
from uuid import UUID

router = APIRouter(prefix="/history", tags=["history"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=HistoryRead)
def create(history: HistoryCreate, db: Session = Depends(get_db)):
    return create_history(db, history)

@router.get("/user/{user_uuid}", response_model=list[HistoryRead])
def list_by_user(user_uuid: UUID, db: Session = Depends(get_db)):
    return get_history_by_user(db, user_uuid)

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.history import HistoryCreate, HistoryRead, HistoryUpdate
from services.history_service import create_history, get_history_by_user, update_history, delete_history
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

@router.put("/{history_uuid}", response_model=HistoryRead)
def update_history_endpoint(history_uuid: UUID, history_data: HistoryUpdate, db: Session = Depends(get_db)):
    updated_history = update_history(db, history_uuid, history_data.model_dump(exclude_unset=True))
    if updated_history is None:
        raise HTTPException(status_code=404, detail="Histórico não encontrado")
    return updated_history

@router.delete("/{history_uuid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_history_endpoint(history_uuid: UUID, db: Session = Depends(get_db)):
    success = delete_history(db, history_uuid)
    if not success:
        raise HTTPException(status_code=404, detail="Histórico não encontrado")
    return {"message": "Histórico deletado com sucesso."}

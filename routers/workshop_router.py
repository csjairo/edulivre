from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.workshop import WorkshopCreate, WorkshopRead
from services.workshop_service import create_workshop, get_workshops, get_workshop_by_id
from uuid import UUID

router = APIRouter(prefix="/workshops", tags=["workshops"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=WorkshopRead)
def create(workshop: WorkshopCreate, db: Session = Depends(get_db)):
    return create_workshop(db, workshop)

@router.get("/", response_model=list[WorkshopRead])
def list_workshops(db: Session = Depends(get_db)):
    return get_workshops(db)

@router.get("/{workshop_uuid}", response_model=WorkshopRead)
def get_workshop(workshop_uuid: UUID, db: Session = Depends(get_db)):
    workshop = get_workshop_by_id(db, workshop_uuid)
    if workshop is None:
        raise HTTPException(status_code=404, detail="Workshop not found")
    return workshop

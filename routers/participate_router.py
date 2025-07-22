from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.participate import ParticipateCreate, ParticipateRead
from services.participate_service import (
    create_participation,
    get_participations_by_student,
    get_participations_by_workshop,
)
from uuid import UUID

router = APIRouter(prefix="/participate", tags=["participate"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ParticipateRead)
def create(participation: ParticipateCreate, db: Session = Depends(get_db)):
    return create_participation(db, participation)

@router.get("/student/{student_uuid}", response_model=list[ParticipateRead])
def list_by_student(student_uuid: UUID, db: Session = Depends(get_db)):
    return get_participations_by_student(db, student_uuid)

@router.get("/workshop/{workshop_uuid}", response_model=list[ParticipateRead])
def list_by_workshop(workshop_uuid: UUID, db: Session = Depends(get_db)):
    return get_participations_by_workshop(db, workshop_uuid)

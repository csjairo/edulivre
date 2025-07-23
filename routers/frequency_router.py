from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.frequency import FrequencyCreate, FrequencyRead
from services.frequency_service import (
    create_frequency,
    get_frequency_by_student,
    get_frequency_by_lesson,
)
from uuid import UUID

router = APIRouter(prefix="/frequency", tags=["frequency"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=FrequencyRead)
def create(frequency: FrequencyCreate, db: Session = Depends(get_db)):
    return create_frequency(db, frequency)

@router.get("/student/{student_uuid}", response_model=list[FrequencyRead])
def list_by_student(student_uuid: UUID, db: Session = Depends(get_db)):
    return get_frequency_by_student(db, student_uuid)

@router.get("/lesson/{lesson_uuid}", response_model=list[FrequencyRead])
def list_by_lesson(lesson_uuid: UUID, db: Session = Depends(get_db)):
    return get_frequency_by_lesson(db, lesson_uuid)

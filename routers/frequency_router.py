from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.frequency import FrequencyCreate, FrequencyRead, FrequencyUpdate
from services.frequency_service import (
    create_frequency,
    get_frequency_by_student_id,
    get_frequency_by_lesson_id,
    get_frequency_by_id,
    update_frequency,
    delete_frequency
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
    return get_frequency_by_student_id(db, student_uuid)

@router.get("/lesson/{lesson_uuid}", response_model=list[FrequencyRead])
def list_by_lesson(lesson_uuid: UUID, db: Session = Depends(get_db)):
    return get_frequency_by_lesson_id(db, lesson_uuid)

@router.get("/{frequency_uuid}", response_model=FrequencyRead)
def get_frequency(frequency_uuid: UUID, db: Session = Depends(get_db)):
    frequency = get_frequency_by_id(db, frequency_uuid)
    if frequency is None:
        raise HTTPException(status_code=404, detail="Frequência não encontrada")
    return frequency

@router.put("/{frequency_uuid}", response_model=FrequencyRead)
def update_frequency_endpoint(frequency_uuid: UUID, frequency_data: FrequencyUpdate, db: Session = Depends(get_db)):
    updated_frequency = update_frequency(db, frequency_uuid, frequency_data.model_dump(exclude_unset=True))
    if updated_frequency is None:
        raise HTTPException(status_code=404, detail="Frequência não encontrada")
    return updated_frequency

@router.delete("/{frequency_uuid}", status_code=status.HTTP_204_NO_CONTENT)
def delete_frequency_endpoint(frequency_uuid: UUID, db: Session = Depends(get_db)):
    success = delete_frequency(db, frequency_uuid)
    if not success:
        raise HTTPException(status_code=404, detail="Frequência não encontrada")
    return {"message": "Frequência deletada com sucesso."}

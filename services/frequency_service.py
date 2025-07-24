from pydantic.types import UUID4
from sqlalchemy.orm import Session
from models.frequency import Frequency, AttendanceStatus
from schemas.frequency import FrequencyCreate
from uuid import UUID
from typing import Optional, Dict, Any

def get_frequency_by_student_id(db: Session, student_id: UUID4) -> Optional[Frequency]:
    return db.query(Frequency).filter(Frequency.student_id == student_id).first()

def get_frequency_by_lesson_id(db: Session, lesson_id: UUID4) -> Optional[Frequency]:
    return db.query(Frequency).filter(Frequency.lesson_id == lesson_id).first()

def create_frequency(db: Session, frequency_data: FrequencyCreate) -> Frequency:
    new_frequency = Frequency(**frequency_data.model_dump())
    db.add(new_frequency)
    db.commit()
    db.refresh(new_frequency)
    return new_frequency

def get_frequency_by_id(db: Session, frequency_uuid: UUID) -> Optional[Frequency]:
    return db.query(Frequency).filter(Frequency.uuid == frequency_uuid).first()

def update_frequency(db: Session, frequency_uuid: UUID, updates: Dict[str, Any]) -> Optional[Frequency]:
    db_frequency = db.query(Frequency).filter(Frequency.uuid == frequency_uuid).first()
    if db_frequency:
        for key, value in updates.items():
            if key == "status" and isinstance(value, str):
                setattr(db_frequency, key, AttendanceStatus(value))
            else:
                setattr(db_frequency, key, value)
        db.commit()
        db.refresh(db_frequency)
    return db_frequency

def delete_frequency(db: Session, frequency_uuid: UUID) -> bool:
    db_frequency = db.query(Frequency).filter(Frequency.uuid == frequency_uuid).first()
    if db_frequency:
        db.delete(db_frequency)
        db.commit()
        return True
    return False

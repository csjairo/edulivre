from sqlalchemy.orm import Session
from models.frequency import Frequency
from schemas.frequency import FrequencyCreate
from uuid import UUID

def create_frequency(db: Session, frequency_data: FrequencyCreate) -> Frequency:
    new_frequency = Frequency(**frequency_data.model_dump())
    db.add(new_frequency)
    db.commit()
    db.refresh(new_frequency)
    return new_frequency

def get_frequency_by_student(db: Session, student_uuid: UUID):
    return db.query(Frequency).filter(Frequency.student_uuid == student_uuid).all()

def get_frequency_by_lesson(db: Session, lesson_uuid: UUID):
    return db.query(Frequency).filter(Frequency.lesson_uuid == lesson_uuid).all()

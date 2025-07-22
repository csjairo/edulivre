from sqlalchemy.orm import Session
from models.participate import Participate
from schemas.participate import ParticipateCreate
from uuid import UUID

def create_participation(db: Session, participation_data: ParticipateCreate) -> Participate:
    new_participation = Participate(**participation_data.model_dump())
    db.add(new_participation)
    db.commit()
    db.refresh(new_participation)
    return new_participation

def get_participations_by_student(db: Session, student_uuid: UUID):
    return db.query(Participate).filter(Participate.student_uuid == student_uuid).all()

def get_participations_by_workshop(db: Session, workshop_uuid: UUID):
    return db.query(Participate).filter(Participate.workshop_uuid == workshop_uuid).all()

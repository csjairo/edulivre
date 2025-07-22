from sqlalchemy.orm import Session
from models.workshop import Workshop
from schemas.workshop import WorkshopCreate
from uuid import UUID

def create_workshop(db: Session, workshop_data: WorkshopCreate) -> Workshop:
    duration = workshop_data.end_date - workshop_data.start_date

    new_workshop = Workshop(
        **workshop_data.model_dump(),
        duration=duration
    )

    db.add(new_workshop)
    db.commit()
    db.refresh(new_workshop)
    return new_workshop

def get_workshops(db: Session):
    return db.query(Workshop).all()

def get_workshop_by_id(db: Session, workshop_uuid: UUID) -> Workshop | None:
    return db.query(Workshop).filter(Workshop.uuid == workshop_uuid).first()

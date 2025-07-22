from sqlalchemy.orm import Session
from models.teacher import Teacher
from schemas.teacher import TeacherCreate
from uuid import UUID

def create_teacher(db: Session, teacher_data: TeacherCreate) -> Teacher:
    new_teacher = Teacher(**teacher_data.model_dump())
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

def get_teachers(db: Session):
    return db.query(Teacher).all()

def get_teacher_by_id(db: Session, teacher_id: int) -> Teacher | None:
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()

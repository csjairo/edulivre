from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.teacher import Teacher
from models.student import Student
from schemas.teacher import TeacherCreate
from uuid import UUID

def create_teacher(db: Session, teacher_data: TeacherCreate) -> Teacher:
    existing_student = db.query(Student).filter(Student.uuid == teacher_data.uuid).first()
    if existing_student:
        raise HTTPException(status_code=409, detail="Este usuário já é um estudante.")

    new_teacher = Teacher(uuid=teacher_data.uuid, **teacher_data.model_dump(exclude={"uuid"}))
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

def get_teachers(db: Session):
    return db.query(Teacher).all()

def get_teacher_by_id(db: Session, teacher_uuid: UUID) -> Teacher | None:
    return db.query(Teacher).filter(Teacher.uuid == teacher_uuid).first()

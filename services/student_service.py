from sqlalchemy.orm import Session
from models.student import Student
from schemas.student import StudentCreate
from uuid import UUID

def create_student(db: Session, student_data: StudentCreate) -> Student:
    new_student = Student(uuid=student_data.uuid, **student_data.model_dump(exclude={"uuid"}))
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def get_students(db: Session):
    return db.query(Student).all()

def get_student_by_id(db: Session, student_uuid: UUID) -> Student | None:
    return db.query(Student).filter(Student.uuid == student_uuid).first()

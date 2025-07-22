from sqlalchemy.orm import Session
from models.lesson import Lesson
from schemas.lesson import LessonCreate
from uuid import UUID

def create_lesson(db: Session, lesson_data: LessonCreate) -> Lesson:
    new_lesson = Lesson(**lesson_data.model_dump())
    db.add(new_lesson)
    db.commit()
    db.refresh(new_lesson)
    return new_lesson

def get_lessons(db: Session):
    return db.query(Lesson).all()

def get_lesson_by_id(db: Session, lesson_uuid: UUID) -> Lesson | None:
    return db.query(Lesson).filter(Lesson.uuid == lesson_uuid).first()

def get_lessons_by_teacher(db: Session, teacher_uuid: UUID):
    return db.query(Lesson).filter(Lesson.teacher_uuid == teacher_uuid).all()

def get_lessons_by_workshop(db: Session, workshop_uuid: UUID):
    return db.query(Lesson).filter(Lesson.workshop_uuid == workshop_uuid).all()

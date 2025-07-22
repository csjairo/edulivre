from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.lesson import LessonCreate, LessonRead
from services.lesson_service import (
    create_lesson,
    get_lessons,
    get_lesson_by_id,
    get_lessons_by_teacher,
    get_lessons_by_workshop
)
from uuid import UUID

router = APIRouter(prefix="/lessons", tags=["lessons"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=LessonRead)
def create(lesson: LessonCreate, db: Session = Depends(get_db)):
    return create_lesson(db, lesson)

@router.get("/", response_model=list[LessonRead])
def list_lessons(db: Session = Depends(get_db)):
    return get_lessons(db)

@router.get("/{lesson_uuid}", response_model=LessonRead)
def get_lesson(lesson_uuid: UUID, db: Session = Depends(get_db)):
    lesson = get_lesson_by_id(db, lesson_uuid)
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson

@router.get("/teacher/{teacher_uuid}", response_model=list[LessonRead])
def list_by_teacher(teacher_uuid: UUID, db: Session = Depends(get_db)):
    return get_lessons_by_teacher(db, teacher_uuid)

@router.get("/workshop/{workshop_uuid}", response_model=list[LessonRead])
def list_by_workshop(workshop_uuid: UUID, db: Session = Depends(get_db)):
    return get_lessons_by_workshop(db, workshop_uuid)

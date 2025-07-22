from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.teacher import TeacherCreate, TeacherRead
from services.teacher_service import create_teacher, get_teachers, get_teacher_by_id

router = APIRouter(prefix="/teachers", tags=["teachers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TeacherRead)
def create(teacher: TeacherCreate, db: Session = Depends(get_db)):
    return create_teacher(db, teacher)

@router.get("/", response_model=list[TeacherRead])
def list_teachers(db: Session = Depends(get_db)):
    return get_teachers(db)

@router.get("/{teacher_id}", response_model=TeacherRead)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = get_teacher_by_id(db, teacher_id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.student import StudentCreate, StudentRead
from services.student_service import create_student, get_students, get_student_by_id
from uuid import UUID

router = APIRouter(prefix="/students", tags=["students"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=StudentRead)
def create(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student)

@router.get("/", response_model=list[StudentRead])
def list_students(db: Session = Depends(get_db)):
    return get_students(db)

@router.get("/{student_uuid}", response_model=StudentRead)
def get_student(student_uuid: UUID, db: Session = Depends(get_db)):
    student = get_student_by_id(db, student_uuid)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

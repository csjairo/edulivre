from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.user import UserCreate, UserRead, UserUpdate
from services.user_service import create_user, get_users, get_user_by_id, update_user
from uuid import UUID

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserRead)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/", response_model=list[UserRead])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: UUID, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserRead)
def update_user_endpoint(user_id: UUID, user_data: UserUpdate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user_data)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from uuid import UUID

def create_user(db: Session, user_data: UserCreate) -> User:
    new_user = User(**user_data.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: UUID) -> User | None:
    return db.query(User).filter(User.uuid == user_id).first()

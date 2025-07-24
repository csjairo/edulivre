from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate, UserUpdate
from uuid import UUID
from typing import Optional

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

def update_user(db: Session, user_id: UUID, user_data: UserUpdate) -> Optional[User]:
    user = db.query(User).filter(User.uuid == user_id).first()

    if not user:
        return None

    update_data = user_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user

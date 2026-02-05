from sqlalchemy.orm import Session
from sqlalchemy import select
from models import User
from schemas import UserCreate

def create_user(db: Session, user: UserCreate):
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_username(db: Session, username: str):
    return db.scalar(select(User).where(User.username == username))
from fastapi import APIRouter, Depends
from db import get_db
from sqlalchemy.orm import Session
from schemas import UserRead, UserCreate
import crud

router_db = APIRouter()

@router_db.post("/user", response_model=UserRead)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router_db.get("/user", response_model=UserRead)
def get_user_endpoint(username: str, db: Session = Depends(get_db)):
    return crud.get_user_by_username(db, username)

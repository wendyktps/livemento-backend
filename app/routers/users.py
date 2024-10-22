from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/users/", response_model=List[schemas.User], name="get_users")
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=schemas.User, name="get_user")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db=db, user_id=user_id)

@router.post("/users/", response_model=schemas.User, name="create_user")
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

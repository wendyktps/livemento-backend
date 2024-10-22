from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from typing import List

router = APIRouter()

@router.get("/shows/", response_model=List[schemas.Show], name="get_shows")
def get_shows(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    shows = crud.get_shows(db=db, skip=skip, limit=limit)
    return shows

@router.get("/shows/{show_id}", response_model=schemas.Show, name="get_show")
def get_show(show_id: int, db: Session = Depends(get_db)):
    return crud.get_show(db=db, show_id=show_id)

@router.post("/shows/", response_model=schemas.Show, name="create_show")
def create_show(show: schemas.ShowBase, db: Session = Depends(get_db)):
    return crud.create_show(db=db, show=show)

@router.post("/users/{user_id}/shows/{show_id}/mark/", response_model=schemas.UserShow)
def mark_show_as_visited(user_id: int, show_id: int, visited: bool, db: Session = Depends(get_db)):
    return crud.mark_show_visited(db=db, user_id=user_id, show_id=show_id, visited=visited)

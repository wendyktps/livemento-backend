from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.get("/shows/{show_id}/reviews/", response_model=List[schemas.Review], name="get_reviews")
def get_reviews(show_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reviews = crud.get_reviews(db=db, show_id=show_id, skip=skip, limit=limit)
    return reviews

@router.post("/reviews/", response_model=schemas.Review, name="create_review")
def create_review(review: schemas.ReviewBase, db: Session = Depends(get_db)):
    return crud.create_review(db=db, review=review)

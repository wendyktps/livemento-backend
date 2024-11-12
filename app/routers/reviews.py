from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db
from app.auth import verify_access_token

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


@router.get("/shows/{show_id}/reviews/", response_model=List[schemas.Review], name="get_reviews")
def get_reviews(show_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reviews = crud.get_reviews(db=db, show_id=show_id, skip=skip, limit=limit)
    return reviews


@router.get("/users/{user_id}/reviews/", response_model=List[schemas.Review])
def get_reviews_by_user(user_id: int, db: Session = Depends(get_db)):
    reviews = crud.get_reviews_by_user(db=db, user_id=user_id)
    return reviews


@router.post("/reviews/", response_model=schemas.Review, name="create_review")
def create_review(review: schemas.ReviewBase, db: Session = Depends(get_db), token: dict = Depends(verify_access_token)):
    user_id = token.get("user_id")
    review.user_id = user_id
    return crud.create_review(db=db, review=review)

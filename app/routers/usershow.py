from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from app.auth import verify_access_token

router = APIRouter()

@router.put("/usershow/{show_id}/going", response_model=schemas.UserShow)
def marked_as_going(show_id: int, db: Session = Depends(get_db), token: str = Depends(verify_access_token)):
    user_id = token.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not authenticated")

    usershow = crud.update_marked_as_going(db, user_id=user_id, show_id=show_id)
    if usershow is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="UserShow record not found")
    return usershow

@router.put("/usershow/{show_id}/attended", response_model=schemas.UserShow)
def marked_as_attended(show_id: int, db: Session = Depends(get_db), token: str = Depends(verify_access_token)):
    user_id = token.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not authenticated")

    usershow = crud.update_marked_as_attended(db, user_id=user_id, show_id=show_id)
    if usershow is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="UserShow record not found")
    return usershow

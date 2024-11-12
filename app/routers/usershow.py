from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from app.auth import verify_access_token

router = APIRouter()

@router.post("/shows/{show_id}/going", response_model=schemas.UserShow)
def mark_as_going(show_id: int, token: str = Depends(verify_access_token), db: Session = Depends(get_db)):
    user_id = token.get("user_id")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return crud.mark_show_as_going(db=db, user_id=user_id, show_id=show_id)

@router.post("/shows/{show_id}/attended", response_model=schemas.UserShow)
def mark_as_attended(show_id: int, token: str = Depends(verify_access_token), db: Session = Depends(get_db)):
    user_id = token.get("user_id")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return crud.mark_show_as_attended(db=db, user_id=user_id, show_id=show_id)

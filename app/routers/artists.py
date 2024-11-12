from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter()


@router.get("/artists/", response_model=list[schemas.Artist])
def get_all_artists(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    artists = crud.get_all_artists(db, skip=skip, limit=limit)
    return artists


@router.get("/artists/by-name/", response_model=list[schemas.Artist])
def get_artists_by_name(name: str, db: Session = Depends(get_db)):
    artists = crud.get_artists_by_name(db, name=name)
    if not artists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No artists found with that name")
    return artists


@router.get("/artists/{artist_id}/", response_model=schemas.Show, name="get_artist")
def get_artist(artist_id: int, db: Session = Depends(get_db)):
    show = crud.get_artist(db=db, show_id=artist_id)
    if show is None:
        raise HTTPException(status_code=404, detail="Show not found")
    return show


@router.post("/artists/", response_model=schemas.Artist, status_code=status.HTTP_201_CREATED)
def create_artist(artist: schemas.ArtistCreate, db: Session = Depends(get_db)):
    db_artist = crud.create_artist(db=db, artist=artist)
    return db_artist

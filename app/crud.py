from sqlalchemy.orm import Session
from app import models, schemas
from passlib.hash import bcrypt
from fastapi import HTTPException, status

def get_shows(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Show).offset(skip).limit(limit).all()


def get_shows_by_name(db: Session, name: str):
    return db.query(models.Show).filter(models.Show.title.ilike(f"%{name}%")).all()


def get_show(db: Session, show_id: int):
    return db.query(models.Show).filter(models.Show.id == show_id).first()


def create_show(db: Session, show: schemas.ShowBase):
    db_show = models.Show(**show.dict())
    db.add(db_show)
    db.commit()
    db.refresh(db_show)
    return db_show


def get_reviews(db: Session, show_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Review).filter(models.Review.show_id == show_id).offset(skip).limit(limit).all()


def get_reviews_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Review).filter(models.Review.user_id == user_id).offset(skip).limit(limit).all()


def create_review(db: Session, review: schemas.ReviewBase):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já está em uso. Tente outro.",
        )
    
    hashed_password = bcrypt.hash(user.password)
    db_user = models.User(email=user.email, name=user.name, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user and bcrypt.verify(password, user.password_hash):
        return user
    return None


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_all_artists(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Artist).offset(skip).limit(limit).all()


def get_artist(db: Session, artist_id: int):
    return db.query(models.Artist).filter(models.Show.id == artist_id).first()


def get_artists_by_name(db: Session, name: str):
    return db.query(models.Artist).filter(models.Artist.name.ilike(f"%{name}%")).all()


def create_artist(db: Session, artist: schemas.ArtistBase):
    db_artist = models.Artist(**artist.dict())
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist


def mark_show_as_going(db: Session, user_id: int, show_id: int):
    user_show = db.query(models.UserShow).filter_by(user_id=user_id, show_id=show_id).first()
    if user_show:
        user_show.going = True
        db.commit()
        db.refresh(user_show)
    else:
        user_show = models.UserShow(user_id=user_id, show_id=show_id, going=True)
        db.add(user_show)
        db.commit()
        db.refresh(user_show)
    return user_show

def mark_show_as_attended(db: Session, user_id: int, show_id: int):
    user_show = db.query(models.UserShow).filter_by(user_id=user_id, show_id=show_id).first()
    if user_show:
        user_show.attended = True
        user_show.going = True
        db.commit()
        db.refresh(user_show)
    else:
        user_show = models.UserShow(user_id=user_id, show_id=show_id, going=True, attended=True)
        db.add(user_show)
        db.commit()
        db.refresh(user_show)
    return user_show

from sqlalchemy.orm import Session
from app import models, schemas
from passlib.hash import bcrypt

def get_shows(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Show).offset(skip).limit(limit).all()

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

def mark_show_as_visited(db: Session, user_id: int, show_id: int, visited: bool):
    user_show = models.UserShow(user_id=user_id, show_id=show_id, visited=visited)
    db.add(user_show)
    db.commit()
    db.refresh(user_show)
    return user_show
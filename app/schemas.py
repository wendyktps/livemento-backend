from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ShowBase(BaseModel):
    title: str
    description: str
    genre: str
    place: str
    date: datetime

class Show(ShowBase):
    id: int
    reviews: List["Review"] = []

    class Config:
        orm_mode = True


class ReviewBase(BaseModel):
    show_id: int
    user_id: int
    rating: float
    comment: Optional[str] = None

class Review(ReviewBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str

class User(UserBase):
    id: int
    reviews: List[Review] = [] 
    shows: List["UserShow"] = []

    class Config:
        orm_mode = True


class UserShowBase(BaseModel):
    show_id: int
    user_id: int
    visited: Optional[bool] = False

class UserShow(UserShowBase):
    id: int

    class Config:
        orm_mode = True

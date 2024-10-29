# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class ShowBase(BaseModel):
    title: str
    description: Optional[str] = None
    image: Optional[str] = None
    genre: str
    place: str
    date: datetime
    opening_artist_id: Optional[int] = None
    setlist: List[str] = []

class Show(ShowBase):
    id: int
    reviews: List["Review"] = []

    class Config:
        orm_mode = True


class ArtistBase(BaseModel):
    name: str
    description: Optional[str] = None
    image: Optional[str] = None
    genre: str
    spotify_link: Optional[str] = None
    apple_music_link: Optional[str] = None

class Artist(ArtistBase):
    id: int

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
    email: EmailStr
    name: str
    image: Optional[str] = None  # Campo opcional para imagem de perfil

class UserCreate(UserBase):
    password: str  # Senha fornecida no registro

class UserLogin(BaseModel):
    email: EmailStr
    password: str  # Senha para autenticação

class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserShowBase(BaseModel):
    show_id: int
    user_id: int
    going: Optional[bool] = False
    attended: Optional[bool] = False

class UserShow(UserShowBase):
    id: int

    class Config:
        orm_mode = True


class ArtistFollowersBase(BaseModel):
    user_id: int
    artist_id: int

class ArtistFollowers(ArtistFollowersBase):
    id: int

    class Config:
        orm_mode = True
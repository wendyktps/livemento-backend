from sqlalchemy import Boolean, DateTime, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Show(Base):
    __tablename__ = "shows"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    genre = Column(String)
    place = Column(String)
    date = Column(DateTime)

    users = relationship("UserShow", back_populates="show")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    show_id = Column(Integer, ForeignKey("shows.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Float)
    comment = Column(String, nullable=True)

    show = relationship("Show", back_populates="reviews")
    user = relationship("User", back_populates="reviews")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    reviews = relationship("Review", back_populates="user")
    shows = relationship("UserShow", back_populates="user")


class UserShow(Base):
    __tablename__ = "user_shows"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    show_id = Column(Integer, ForeignKey("shows.id"))
    visited = Column(Boolean, default=False)

    user = relationship("User", back_populates="shows")
    show = relationship("Show", back_populates="users")
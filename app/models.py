from sqlalchemy import JSON, Boolean, DateTime, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Text
from app.database import Base


class Show(Base):
    __tablename__ = "shows"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
    title = Column(String, index=True)
    description = Column(Text)
    genre = Column(String)
    place = Column(String)
    date = Column(DateTime)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    opening_artist_id = Column(Integer, ForeignKey(
        "artists.id"), nullable=True, default=None)
    setlist = Column(JSON)

    users = relationship("UserShow", back_populates="show")
    reviews = relationship("Review", back_populates="show")
    artist = relationship("Artist", foreign_keys=[artist_id])
    opening_artist = relationship("Artist", foreign_keys=[opening_artist_id])


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
    name = Column(String, index=True)
    description = Column(Text)
    genre = Column(String)
    spotify = Column(String)
    apple_music = Column(String)

    followers = relationship("ArtistFollowers", back_populates="artist")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)

    reviews = relationship("Review", back_populates="user")
    shows = relationship("UserShow", back_populates="user")
    followed_artists = relationship("ArtistFollowers", back_populates="user")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    show_id = Column(Integer, ForeignKey("shows.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Float)
    comment = Column(Text, nullable=True)

    show = relationship("Show", back_populates="reviews")
    user = relationship("User", back_populates="reviews")


class UserShow(Base):
    __tablename__ = "user_shows"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    show_id = Column(Integer, ForeignKey("shows.id"))
    going = Column(Boolean, default=False)
    attended = Column(Boolean, default=False)

    user = relationship("User", back_populates="shows")
    show = relationship("Show", back_populates="users")


class ArtistFollowers(Base):
    __tablename__ = "artist_followers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    artist_id = Column(Integer, ForeignKey("artists.id"))

    user = relationship("User", back_populates="followed_artists")
    artist = relationship("Artist", back_populates="followers")

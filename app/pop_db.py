from sqlalchemy.orm import Session
from app.database import engine
from app.models import Base, User, Artist, Show, Review, UserShow, ArtistFollowers
from datetime import datetime, timedelta
import random

def populate_database(db: Session):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    users = [
        User(image="user1.png", name="wendy", email="w@a.com", password_hash="123"),
        User(image="user2.png", name="lucca", email="l@ea.com", password_hash="1232"),
        User(image="user3.png", name="anna", email="a@a.com", password_hash="123"),
    ]
    db.add_all(users)
    db.commit()

    artists = [
        Artist(image="https://abrir.link/wCPWG", name="Post Malone", description="um moço ai", genre="Trap", 
               spotify="https://open.spotify.com/intl-pt/artist/246dkjvS1zLTtiykXe5h60", 
               apple_music="https://music.apple.com/br/artist/post-malone/966309175"),
        
        Artist(image="https://abrir.link/fNxuS", name="Iron Maiden", description="airo meide", genre="Rock", 
               spotify="https://open.spotify.com/intl-pt/artist/6mdiAmATAx73kdxrNrnlao", 
               apple_music="https://music.apple.com/br/artist/iron-maiden/546381"),
        
        Artist(image="https://abrir.link/kuIsW", name="Toto", description="só tem uma música", genre="Pop", 
               spotify="https://open.spotify.com/intl-pt/artist/0PFtn5NtBbbUNbU9EAmIWF", 
               apple_music="https://music.apple.com/br/artist/toto/462614"),
    ]
    db.add_all(artists)
    db.commit()

    shows = [
        Show(
            image="https://abrir.link/wCPWG", 
            title="Beerbongs & Bentleys Live",
            description="Show épico com Post Malone apresentando seus maiores sucessos.",
            genre="Trap",
            place="Trap Arena",
            date=datetime.utcnow() + timedelta(days=10),
            artist_id=1,  
            opening_artist_id=2,  
            setlist=["Rockstar", "Circles", "Congratulations"]
        ),
        Show(
            image="https://abrir.link/fNxuS",  # Imagem de Iron Maiden
            title="Legacy of the Beast Tour",
            description="Iron Maiden detonando com seus maiores clássicos do heavy metal.",
            genre="Rock",
            place="Metal Arena",
            date=datetime.utcnow() + timedelta(days=20),
            artist_id=2,  
            opening_artist_id=None, 
            setlist=["The Trooper", "Fear of the Dark", "Run to the Hills"]
        ),
        Show(
            image="https://abrir.link/kuIsW", 
            title="Africa Live",
            description="Toto em um show exclusivo tocando seus sucessos como Africa e Rosanna.",
            genre="Pop",
            place="Classic Hall",
            date=datetime.utcnow() + timedelta(days=30),
            artist_id=3,  
            opening_artist_id=1,  
            setlist=["Africa", "Rosanna", "Hold the Line"]
        ),
    ]

    db.add_all(shows)
    db.commit()

    reviews = [
        Review(show_id=1, user_id=1, rating=4.5, comment="Amazing performance by Post Malone!"),
        Review(show_id=2, user_id=2, rating=5.0, comment="Iron Maiden was incredible!"),
        Review(show_id=3, user_id=3, rating=3.5, comment="Toto's set was good, but I expected more."),
        Review(show_id=1, user_id=2, rating=4.0, comment="Post Malone's energy was contagious!"),
        Review(show_id=2, user_id=3, rating=4.8, comment="Iron Maiden brought the house down!"),
        Review(show_id=3, user_id=1, rating=3.0, comment="Toto was decent, but not my favorite."),
    ]
    
    db.add_all(reviews)
    db.commit()

    user_shows = [
        UserShow(user_id=1, show_id=1, going=True, attended=False),
        UserShow(user_id=2, show_id=2, going=True, attended=True),
        UserShow(user_id=3, show_id=3, going=False, attended=False),
    ]
    
    db.add_all(user_shows)
    db.commit()

    artist_followers = [
        ArtistFollowers(user_id=1, artist_id=1),
        ArtistFollowers(user_id=2, artist_id=2),
        ArtistFollowers(user_id=3, artist_id=3),
        ArtistFollowers(user_id=1, artist_id=2),
        ArtistFollowers(user_id=3, artist_id=3),
    ]
    
    db.add_all(artist_followers)
    db.commit()

    print("Database populated with test data!")


if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    with SessionLocal() as session:
        populate_database(session)

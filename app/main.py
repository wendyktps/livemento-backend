from fastapi import FastAPI
from app.routers import shows, reviews, auth
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(shows.router, prefix="/shows", tags=["shows"])
app.include_router(reviews.router, prefix="/reviews", tags=["reviews"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])

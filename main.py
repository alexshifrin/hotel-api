from dataclasses import dataclass

from fastapi import FastAPI

from hotel.db.engine import init_db, DBSession
from hotel.db.models import DBRoom
from hotel.routers import rooms

app = FastAPI()

DB_FILE = "sqlite:///hotel.db"

@app.on_event("startup")
def startup_event():
    init_db(DB_FILE)

@app.get("/")
def root():
    return "The server works!"

app.include_router(rooms.router)

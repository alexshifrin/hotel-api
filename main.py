from fastapi import FastAPI

from hotel.db.engine import init_db
from hotel.routers import rooms, customers

app = FastAPI()

DB_FILE = "sqlite:///hotel.db"

@app.on_event("startup")
def startup_event():
    init_db(DB_FILE)

@app.get("/")
def root():
    return "The server works!"

app.include_router(rooms.router)
app.include_router(customers.router)

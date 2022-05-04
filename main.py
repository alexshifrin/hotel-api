from dataclasses import dataclass
from datetime import date

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "The server works!"

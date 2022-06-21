from fastapi import FastAPI, Depends
from .repository import client_repo
from sqlalchemy.orm import Session
from .database import get_db, engine, Base

app = FastAPI()

Base.metadata.create_all(engine)


@app.get("/clients")
def get_clients(db: Session = Depends(get_db)):
    return client_repo.get_all(db)
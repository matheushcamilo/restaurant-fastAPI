from fastapi import FastAPI, Depends
from .repository import client_repo
from sqlalchemy.orm import Session
from .database import get_db, engine, Base
from . import schemas

app = FastAPI()

Base.metadata.create_all(engine)


@app.get("/clients")
def get_clients(db: Session = Depends(get_db)):
    return client_repo.get_all(db)

@app.post("/clients")
def create_client(request: schemas.Client, db: Session = Depends(get_db)):
    return client_repo.create(request, db)    
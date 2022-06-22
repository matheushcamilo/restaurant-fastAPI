from fastapi import FastAPI, Depends
from .repository import client_repo
from sqlalchemy.orm import Session
from .database import get_db, engine, Base
from . import schemas

app = FastAPI()

Base.metadata.create_all(engine)

#TODO Fix order of Json response
@app.get("/clients")
def get_clients(db: Session = Depends(get_db)):
    return client_repo.get_all(db)

@app.get("/clients/{first_name}-{last_name}")
def get_client_by_name(first_name: str, last_name: str, db: Session = Depends(get_db)):
    return client_repo.get_by_name(first_name, last_name, db)


@app.post("/clients")
def create_client(request: schemas.Client, db: Session = Depends(get_db)):
    return client_repo.create(request, db)    
    
from urllib import request
from fastapi import FastAPI, Depends
from .repository import client_repo, order_repo
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
    

@app.get("/orders") 
def get_orders(db: Session = Depends(get_db)):
    return order_repo.get_all(db)   

@app.get("/orders/{id}")
def get_order_by_id(id: int, db: Session = Depends(get_db)):
    return order_repo.get_by_id(id, db)  

@app.post("/orders")
def create_new_order(request: schemas.Order, db: Session = Depends(get_db)):
    return order_repo.create_order(request, db)
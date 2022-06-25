from fastapi import FastAPI, Depends, status, Response, HTTPException
from .repository import client_repo, order_repo
from sqlalchemy.orm import Session
from .database import get_db, engine, Base
from . import schemas

app = FastAPI()

Base.metadata.create_all(engine)


#-----------------Endpoits to deal with clients --------------------------
@app.get("/clients", status_code=200)
def get_all_clients(db: Session = Depends(get_db)):
    clients = client_repo.get_all(db)
    if not clients:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No clients found')
    return clients

@app.post("/clients", status_code=status.HTTP_201_CREATED)
def create_client(request: schemas.Client, db: Session = Depends(get_db)):
    return client_repo.create(request, db)    

@app.get("/clients/{first_name}-{last_name}")
def get_client_by_name(first_name: str, last_name: str, db: Session = Depends(get_db)):
    client = client_repo.get_by_name(first_name, last_name, db)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"There is no client by the name of '{first_name} {last_name}'")
    return client    

@app.delete('/clients/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_client_by_id(id: int, db: Session = Depends(get_db)):
    deleted_client = client_repo.delete_by_id(id, db)
    if not deleted_client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"There is no client with id {id}") 
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
@app.put('/clients/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_client_by_id(id: int, request: schemas.Client, db: Session = Depends(get_db)):
    updated_client = client_repo.update_by_id(id, request, db) 
    if updated_client is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no client with id '{id}'")
    return f"Client with id '{id}' has been successfully updated"
    
#------------------------- Endpoits to deal with orders ------------------------    

@app.get("/orders") 
def get_orders(db: Session = Depends(get_db)):
    orders = order_repo.get_all(db) 
    if not orders:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No orders found")
    return orders  
    
@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(request: schemas.Order, db: Session = Depends(get_db)):
    return order_repo.create(request, db)    

@app.get("/orders/{id}")
def get_order_by_id(id: int, db: Session = Depends(get_db)):
    order = order_repo.get_by_id(id, db)  
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"There is no order with id {id}")
    return order

@app.delete('/orders/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_order_by_id(id: int, db: Session = Depends(get_db)):
    deleted_client = order_repo.delete_by_id(id, db)
    if not deleted_client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"There is no order with id {id}")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/orders/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_order_by_id(id: int, request: schemas.Order, db: Session = Depends(get_db)):
    updated_order = order_repo.update_by_id(id, request, db) 
    if updated_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no order with id '{id}'")
    return f"Order with id '{id}' has been successfully updated"

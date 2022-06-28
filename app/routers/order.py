from app.oauth2 import get_current_user
from .. import database, schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..repository import order_repository
from typing import List

get_db = database.get_db

router = APIRouter(
    prefix="/orders",
    tags=['Orders']
)


@router.get("/", response_model=List[schemas.OrderResponseModel]) 
def get_orders(db: Session = Depends(get_db), get_current_user: schemas.Client = Depends(get_current_user)):
    orders = order_repository.get_all(db) 
    if not orders:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No orders found")
    return orders  
    
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.OrderResponseModel)
def create_order(request: schemas.Order, db: Session = Depends(get_db), get_current_user: schemas.Client = Depends(get_current_user)):
    return order_repository.create(request, db)    

@router.get("/{id}", response_model=schemas.OrderResponseModel)
def get_order_by_id(id: int, db: Session = Depends(get_db), get_current_user: schemas.Client = Depends(get_current_user)):
    order = order_repository.get_by_id(id, db)  
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"There is no order with id '{id}'")
    return order

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_order_by_id(id: int, db: Session = Depends(get_db), get_current_user: schemas.Client = Depends(get_current_user)):
    deleted_client = order_repository.delete_by_id(id, db)
    if not deleted_client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"There is no order with id {id}")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_order_by_id(id: int, request: schemas.Order, db: Session = Depends(get_db), get_current_user: schemas.Client = Depends(get_current_user)):
    updated_order = order_repository.update_by_id(id, request, db) 
    if updated_order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no order with id '{id}'")
    return f"The order with id '{id}' has been updated successfully"

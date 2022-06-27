from .. import database, schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..repository import client_repo
from typing import List

router = APIRouter(
    prefix="",
    tags=['Clients']
)

get_db = database.get_db

@router.get("/", status_code=200, response_model=List[schemas.ClientResponseModel])
def get_all_clients(db: Session = Depends(get_db)):
    clients = client_repo.get_all(db)
    if not clients:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No clients found')
    return clients

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ClientResponseModel)
def create_client(request: schemas.Client, db: Session = Depends(get_db)):
    return client_repo.create(request, db)    

@router.get("/{first_name}-{last_name}", response_model=schemas.ClientResponseModel)
def get_client_by_name(first_name: str, last_name: str, db: Session = Depends(get_db)):
    client = client_repo.get_by_name(first_name, last_name, db)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"There is no client by the name of '{first_name} {last_name}'")
    return client    

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_client_by_id(id: int, db: Session = Depends(get_db)):
    deleted_client = client_repo.delete_by_id(id, db)
    if not deleted_client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"There is no client with id {id}") 
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_client_by_id(id: int, request: schemas.Client, db: Session = Depends(get_db)):
    updated_client = client_repo.update_by_id(id, request, db) 
    if updated_client is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no client with id '{id}'")
    return f"The client with id '{id}' has been updated successfully"
from sqlalchemy.orm import Session
from .. import models, schemas


def get_all(db: Session):
    clients = db.query(models.Client).all()
    return clients

def get_by_name(first_name, last_name, db: Session):
    return db.query(models.Client).filter(models.Client.first_name == first_name,
    models.Client.last_name == last_name).first()

def delete_by_id(id, db: Session):
    client = db.query(models.Client).filter(models.Client.id == id).delete(synchronize_session=False) 
    db.commit()
    return client

def update_by_id(id, request: schemas.Client, db: Session):    
    client = db.query(models.Client).filter(models.Client.id == id)
    if not client.first():
        return None
    client.update(request.dict())
    db.commit()
    return 'updated'
    
def create(request: schemas.Client, db: Session):
    new_client = models.Client(first_name=request.first_name, last_name=request.last_name,
    gender=request.gender)
    db.add(new_client)
    db.commit()
    return new_client
    
           
    
from sqlalchemy.orm import Session
from .. import models, schemas


def get_all(db: Session):
    clients = db.query(models.Client).all()
    return clients


def get_by_name(first_name, last_name, db: Session):
    return db.query(models.Client).filter(models.Client.first_name == first_name and
    models.Client.last_name == last_name).first()

def create(request: schemas.Client, db: Session):
    new_client = models.Client(first_name=request.first_name, last_name=request.last_name,
    gender=request.gender)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client
   
        
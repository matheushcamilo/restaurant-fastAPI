from sqlalchemy.orm import Session
from .. import models, schemas

def get_all(db: Session):
    return db.query(models.Order).all()

def get_by_id(id, db: Session):
    return db.query(models.Order).filter(models.Order.id == id).first()    

def create_order(request: schemas.Order, db: Session):
    new_order = models.Order(description=request.description)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order    

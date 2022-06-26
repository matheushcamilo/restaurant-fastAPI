from sqlalchemy.orm import Session
from .. import models, schemas

def get_all(db: Session):
    return db.query(models.Order).all()

def get_by_id(id, db: Session):
    return db.query(models.Order).filter(models.Order.id == id).first()    

def delete_by_id(id, db: Session):
    order = db.query(models.Order).filter(models.Order.id == id).delete(synchronize_session=False) 
    db.commit()
    return order

def update_by_id(id, request: schemas.Order, db: Session):    
    order = db.query(models.Order).filter(models.Order.id == id)
    if not order.first():
        return None
    order.update(request.dict())
    db.commit()
    return 'updated'

def create(request: schemas.Order, db: Session):
    new_order = models.Order(description=request.description)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order    



from sqlalchemy.orm import Session
from .. import models, schemas


def get_all(db: Session):
    clients = db.query(models.Client).all()
    return clients
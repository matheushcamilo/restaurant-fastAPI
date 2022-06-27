from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, status, Depends
from .. import schemas, models, database
from ..hashing import Hash

router = APIRouter()


@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.Client).filter(models.Client.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")    
    return f"User {user.first_name} has been authenticated"
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, status, Depends
from .. import schemas, models, database
from ..hashing import Hash
from ..JWTtoken import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter()


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.Client).filter(models.Client.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
from fastapi import APIRouter, Depends
from ..schemas import jobSeekerLogin
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from fastapi import status, HTTPException
from ..hashing import Hash
from ..token import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['JobSeeker Login']
)

@router.post('/jobseeker_login')
def jobseeker_login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    jobseeker = db.query(models.JobSeeker).filter(models.JobSeeker.email == request.username).first()
    if not jobseeker:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Jobseeker with email {request.username} not found')
    if not Hash.verify(jobseeker.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect password')
    
    access_token = create_access_token(data={"sub": jobseeker.email})
    return {"access_token": access_token, "token_type": "bearer"}




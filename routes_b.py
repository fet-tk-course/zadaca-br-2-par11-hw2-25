from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from models_b import Adopter, AdopterCreate, AdopterUpdate
from typing import List, Optional
from database import get_session

router = APIRouter(prefix="/adopters", tags=["Adopters"])

@router.post("/", response_model=Adopter, status_code=status.HTTP_201_CREATED)
def create_adopter(adopter: AdopterCreate, session: Session = Depends(get_session)):
    # Kreiranje novog udomitelja
    db_adopter = Adopter.model_validate(adopter)
    session.add(db_adopter)
    session.commit()
    session.refresh(db_adopter)
    return db_adopter
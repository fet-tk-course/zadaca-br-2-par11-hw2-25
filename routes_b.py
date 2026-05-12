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

@router.get("/", response_model=List[Adopter])
def read_adopters(experience: Optional[bool] = None, session: Session = Depends(get_session)):
    statement = select(Adopter)
    if experience is not None:
        statement = statement.where(Adopter.has_experience == experience)
    return session.exec(statement).all()

@router.get("/{adopter_id}", response_model=Adopter)
def read_adopter(adopter_id: int, session: Session = Depends(get_session)):
    adopter = session.get(Adopter, adopter_id)
    if not adopter:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Udomitelj nije pronađen")
    return adopter

@router.put("/{adopter_id}", response_model=Adopter)
def replace_adopter(adopter_id: int, adopter_update: AdopterCreate, session: Session = Depends(get_session)):
    adopter = session.get(Adopter, adopter_id)
    if not adopter:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Udomitelj nije pronađen")
    
    adopter_data = adopter_update.model_dump()
    for key, value in adopter_data.items():
        setattr(adopter, key, value)
    
    session.add(adopter)
    session.commit()
    session.refresh(adopter)
    return adopter

@router.patch("/{id}", response_model=Adopter)
def update_adopter_partial(id: int, adopter_update: AdopterUpdate, session: Session = Depends(get_session)):
    # 1. Pronađi postojeći resurs u bazi
    db_adopter = session.get(Adopter, id)
    
    if not db_adopter:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Udomitelj nije pronađen")
    
    update_data = adopter_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_adopter, key, value)
    
    session.add(db_adopter)
    session.commit()
    session.refresh(db_adopter)
    return db_adopter


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_adopter(id: int, session: Session = Depends(get_session)):
    # Brisanje resursa
    adopter = session.get(Adopter, id)
    if not adopter:
        raise HTTPException(status_code=404, detail="Adopter not found")
    session.delete(adopter)
    session.commit()
    return None
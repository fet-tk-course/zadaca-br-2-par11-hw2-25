from sqlmodel import SQLModel, Field
from typing import Optional

class Animal(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    species: str
    age: int
    vaccinated: bool
    adoption_fee: float
    description: Optional[str] = None


class AnimalCreate(SQLModel):
    name: str
    species: str
    age: int
    vaccinated: bool
    adoption_fee: float
    description: Optional[str] = None


class AnimalUpdate(SQLModel):
    name: Optional[str] = None
    species: Optional[str] = None
    age: Optional[int] = None
    vaccinated: Optional[bool] = None
    adoption_fee: Optional[float] = None
    description: Optional[str] = None
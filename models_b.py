from sqlmodel import SQLModel, Field
from typing import Optional

class Adopter(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    age: int
    email: str
    phone_number: int
    has_experience: bool = False

class AdopterCreate(SQLModel):
    first_name: str
    last_name: str
    age: int
    email: str
    phone_number: int
    has_experience: bool = False

class AdopterUpdate(SQLModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    phone_number: Optional[int] = None
    has_experience: Optional[bool] = None

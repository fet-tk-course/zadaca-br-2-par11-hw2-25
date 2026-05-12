from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import field_validator

class Adopter(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    age: int
    email: str
    phone_number: str
    has_experience: bool = False

class AdopterCreate(SQLModel):
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    age: int
    email: str
    phone_number: str
    has_experience: bool = False

    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Email adresa mora sadržavati znak '@'")
        return value

class AdopterUpdate(SQLModel):
    first_name: Optional[str] = Field(default=None, min_length=1)
    last_name: Optional[str] = Field(default=None, min_length=1)
    age: Optional[int] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    has_experience: Optional[bool] = None

    @field_validator("email")
    @classmethod    
    def validate_email_update(cls, value):
        if value is not None and "@" not in value:
            raise ValueError("Email adresa mora sadržavati znak '@'")
        return value
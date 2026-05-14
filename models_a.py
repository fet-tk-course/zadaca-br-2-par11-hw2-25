from sqlmodel import SQLModel, Field
from typing import Optional

from pydantic import field_validator


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

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Name must not be empty")
        return value.strip()

    @field_validator("species")
    @classmethod
    def species_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Species must not be empty")
        return value.strip()

    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Age must be greater than zero")
        return value

    @field_validator("adoption_fee")
    @classmethod
    def adoption_fee_must_not_be_negative(cls, value):
        if value < 0:
            raise ValueError("Adoption fee must not be negative")
        return value


class AnimalUpdate(SQLModel):
    name: Optional[str] = None
    species: Optional[str] = None
    age: Optional[int] = None
    vaccinated: Optional[bool] = None
    adoption_fee: Optional[float] = None
    description: Optional[str] = None

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, value):
        if value is not None and not value.strip():
            raise ValueError("Name must not be empty")
        return value.strip() if value is not None else value

    @field_validator("species")
    @classmethod
    def species_must_not_be_empty(cls, value):
        if value is not None and not value.strip():
            raise ValueError("Species must not be empty")
        return value.strip() if value is not None else value

    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, value):
        if value is not None and value <= 0:
            raise ValueError("Age must be greater than zero")
        return value

    @field_validator("adoption_fee")
    @classmethod
    def adoption_fee_must_not_be_negative(cls, value):
        if value is not None and value < 0:
            raise ValueError("Adoption fee must not be negative")
        return value
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from database import get_session

router = APIRouter(prefix="/resursi_a", tags=["Resurs A"])

GET /animals
GET /animals/{animal_id}
POST /animals
PUT /animals/{animal_id}
PATCH /animals/{animal_id}
DELETE /animals/{animal_id}
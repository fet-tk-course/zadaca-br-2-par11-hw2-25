from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from database import get_session
from models_a import Animal, AnimalCreate, AnimalUpdate


router = APIRouter(prefix="/animals", tags=["Animals"])


@router.get("/", response_model=list[Animal])
def get_animals(species: str | None = None, session: Session = Depends(get_session)):
    statement = select(Animal)

    if species:
        statement = statement.where(Animal.species == species)

    animals = session.exec(statement).all()
    return animals


@router.get("/statistics")
def get_animals_statistics(session: Session = Depends(get_session)):
    animals = session.exec(select(Animal)).all()

    total_animals = len(animals)
    vaccinated_animals = sum(1 for animal in animals if animal.vaccinated)
    unvaccinated_animals = total_animals - vaccinated_animals

    if total_animals == 0:
        average_adoption_fee = 0
    else:
        total_adoption_fee = sum(animal.adoption_fee for animal in animals)
        average_adoption_fee = total_adoption_fee / total_animals

    return {
        "total_animals": total_animals,
        "vaccinated_animals": vaccinated_animals,
        "unvaccinated_animals": unvaccinated_animals,
        "average_adoption_fee": average_adoption_fee,
    }


@router.get("/{animal_id}", response_model=Animal)
def get_animal(animal_id: int, session: Session = Depends(get_session)):
    animal = session.get(Animal, animal_id)

    if not animal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Animal not found",
        )

    return animal


@router.post("/", response_model=Animal, status_code=status.HTTP_201_CREATED)
def create_animal(animal_data: AnimalCreate, session: Session = Depends(get_session)):
    duplicate_statement = select(Animal).where(
        Animal.name == animal_data.name,
        Animal.species == animal_data.species,
    )
    existing_animal = session.exec(duplicate_statement).first()

    if existing_animal:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Animal with the same name and species already exists",
        )

    animal = Animal.model_validate(animal_data)

    session.add(animal)
    session.commit()
    session.refresh(animal)

    return animal


@router.put("/{animal_id}", response_model=Animal)
def replace_animal(
    animal_id: int,
    animal_data: AnimalCreate,
    session: Session = Depends(get_session),
):
    animal = session.get(Animal, animal_id)

    if not animal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Animal not found",
        )

    animal.name = animal_data.name
    animal.species = animal_data.species
    animal.age = animal_data.age
    animal.vaccinated = animal_data.vaccinated
    animal.adoption_fee = animal_data.adoption_fee
    animal.description = animal_data.description

    session.add(animal)
    session.commit()
    session.refresh(animal)

    return animal


@router.patch("/{animal_id}", response_model=Animal)
def update_animal(
    animal_id: int,
    animal_data: AnimalUpdate,
    session: Session = Depends(get_session),
):
    animal = session.get(Animal, animal_id)

    if not animal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Animal not found",
        )

    animal_update_data = animal_data.model_dump(exclude_unset=True)

    for key, value in animal_update_data.items():
        setattr(animal, key, value)

    session.add(animal)
    session.commit()
    session.refresh(animal)

    return animal


@router.delete("/{animal_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_animal(animal_id: int, session: Session = Depends(get_session)):
    animal = session.get(Animal, animal_id)

    if not animal:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Animal not found",
        )

    session.delete(animal)
    session.commit()

    return None
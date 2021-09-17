from fastapi import APIRouter
from schemas.bird import Bird
import json
from fastapi import HTTPException

from models.bird_model import Bird as BirdRepo

repo = BirdRepo()

router = APIRouter(
    prefix="/birds",
    tags=["Bird"],
    responses={404: {"Bird": "Not found"}},
)

# with open('../../birds.json', 'r') as f:
#   birds = json.load(f)

# @router.get("")
# def getBirds():
#     return birds

# @router.get("/{bird_id}")
# async def getBird(bird_id):
#     return list(filter(lambda bird: Bird(**bird).id == bird_id, birds)) # Filter the list of birds, and only return the bird we need.

@router.get("")
def getBirds():
    objects = repo.get_all()
    if objects is None:
        raise HTTPException(status_code=400, detail="Something went wrong here!")
    return objects

@router.post("")
def postBird(bird: Bird):
    created_object = repo.create(bird)
    if created_object is None:
        raise HTTPException(status_code=400, detail=f"A bird like that already exists.")
    return created_object
from fastapi import APIRouter
from schemas.bird import Bird
import json

router = APIRouter(
    prefix="/birds",
    tags=["Bird"],
    responses={404: {"Bird": "Not found"}},
)

with open('../../birds.json', 'r') as f:
  birds = json.load(f)

@router.get("")
def getBirds():
    return birds

@router.get("/{bird_id}")
async def getBird(bird_id):
    return list(filter(lambda bird: Bird(**bird).id == bird_id, birds)) # Filter the list of birds, and only return the bird we need.

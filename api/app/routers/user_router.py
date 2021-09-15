
from fastapi import APIRouter
from schemas.user import User

router = APIRouter(
    prefix="/users",
    tags=["User"],
    responses={404: {"User": "Not found"}},
)

users = [
    {
        "name": "Nathan Segers",
        "locationOfResidence": "Aalst",
        "age": 23,
        "gender": "M",
        "registrationDate": "2021-09-15 12:00:00"
    }
]

@router.get("/users")
def getUsers():
    return users

@router.post("/user")
def postUser(user: User):
  users.append(user)
  return users
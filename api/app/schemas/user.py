from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    uuid: str
    name: str
    locationOfResidence: str
    age: int
    gender: str
    registrationDate: datetime

    def sayHello(self):
        print(f"{self.name} is flying by.")
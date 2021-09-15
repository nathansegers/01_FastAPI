from pydantic import BaseModel


class Bird(BaseModel):
    uuid: str
    id: str
    name: str
    short: str
    image: str
    recon: list
    food: dict
    see: str

    def sayHello(self):
        print(f"{self.name} is flying by.")
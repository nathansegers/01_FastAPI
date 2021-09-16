from datetime import datetime
from database import Base
import uuid

from sqlalchemy import Column, String, Text, Integer, DateTime

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = 'users'

    uuid = Column(String(100), name="uuid", primary_key=True, default=generate_uuid)
    name = Column(String(100))
    locationOfResidence = Column(String(100))
    age = Column(Integer())
    gender = Column(String(1)) # M/V/X
    registrationDate = Column(DateTime())

    def __init__(self, *,
        uuid: str  = generate_uuid(),
        name: str = '',
        locationOfResidence: str = '',
        age: int = 0,
        gender: str = '',
        registrationDate: datetime = datetime.now(),
    ):
        self.uuid = uuid
        self.name = name
        self.locationOfResidence = locationOfResidence
        self.age = age
        self.gender = gender
        self.registrationDate = registrationDate

    def __repr__(self):
        return '<User {}>'.format(self.name)
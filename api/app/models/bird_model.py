from database import Base
import uuid

from sqlalchemy import Column, String, Text

def generate_uuid():
    return str(uuid.uuid4())

import json
import sqlalchemy
from sqlalchemy.types import TypeDecorator

SIZE = 5120

class TextPickleType(TypeDecorator):

    impl = sqlalchemy.Text(SIZE)

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value

class Bird(Base):
    __tablename__ = 'birds'

    uuid = Column(String(100), name="uuid", primary_key=True, default=generate_uuid)
    id = Column(String(100), unique=True)
    name = Column(String(100))
    short = Column(Text)
    image = Column(String(100))
    recon = Column(TextPickleType())
    food = Column(TextPickleType())
    see = Column(Text)

    def __init__(self, *,
        uuid: str  = generate_uuid(),
        id: str = '',
        name: str = '',
        short: str = '',
        image: str = '',
        recon: str = '',
        food: str = '',
        see: str = ''
    ):
        self.uuid = uuid
        self.id = id
        self.name = name
        self.short = short
        self.image = image
        self.recon = recon
        self.food = food
        self.see = see

    def __repr__(self):
        return '<Bird {}>'.format(self.name)
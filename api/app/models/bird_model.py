from database import (
    Base,
    db # db is our database connector
)
import uuid

from schemas.bird import Bird as BirdSchema

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

        self.model = Bird
        self.schema = BirdSchema

    def __repr__(self):
        return '<Bird {}>'.format(self.name)

    def get_by(self, **kwargs):
        try:
            db_object = db.query(self.model).filter_by(**kwargs).first()
            if db_object:
                return self.schema.from_orm(db_object)
            else:
                print(f"No {self.model} was found!")
                return None
        except Exception as e:
            print(f"Error while getting {self.model}.")
            print(e)
            db.rollback()

    def get_many(self, **kwargs):
        try:
            db_objects = db.query(self.model).filter_by(**kwargs).all()
            if db_objects:
                return db_objects
            else:
                print(f"No {self.model} was found!")
                return None
        except Exception as e:
            print(f"Error while getting {self.model}.")
            print(e)
            db.rollback()

    def get_all(self):
        try:
            db_objects = db.query(self.model).all()
            if db_objects:
                return db_objects
            else:
                print(f"No {self.model} was found!")
                return None
        except Exception as e:
            print(f"Error while getting all {self.model}s.")
            print(e)
            db.rollback()

    def create(self, obj: BirdSchema):
        try:
            obj_in_db = self.get_by(name=obj.name)
            if obj_in_db is None:
                print(f"No {self.model} was found with name {obj.name}!")

                new_obj = self.model(**obj.dict())
                db.add(new_obj)
                db.commit()

                print(f"{self.model} has been added to the database!")
                obj = self.schema.from_orm(new_obj)
            else:
                obj = None
                print(f"A {self.model} already exists.")

            return obj

        except Exception as e:
            print(f"Error while creating {self.model}.")
            print("Rolling back the database commit.")
            print(e)
            db.rollback()

    def update(self, new_obj: BirdSchema):
        try:
            old_obj = db.query(self.model).filter_by(uuid=new_obj.uuid).first()

            for key, value in new_obj.dict(exclude_unset=True).items():
                if getattr(old_obj, key) != value: ## difference
                    setattr(old_obj, key, value)
                    
            db.commit()
            movement = self.schema.from_orm(old_obj)
            return movement

        except Exception as e:
            print(f"Error while updating {self.model}.")
            print(e)
            print("Rolling back the database commit.")
            db.rollback()

    
    def delete(self, old_obj: BirdSchema):
        try:
            num_rows_deleted = db.query(self.model).filter_by(uuid=old_obj.uuid).delete()
            print(f"Deleted {num_rows_deleted} items.")
            db.commit()
            return num_rows_deleted
        except Exception as e:
            print(f"Error while deleting {self.model}.")
            print(e)
            print("Rolling back the database commit.")
            db.rollback()
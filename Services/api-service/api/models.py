from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Character(Base):
    __tablename__ = 'Character'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer,nullable=False)
    hair_color = Column(String(128), nullable=False)
    skin_color = Column(String(128), nullable=False)
    eye_color = Column(String(128), nullable=False)
    birth_year = Column(Integer,nullable=False)

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'height' : self.height,
            'mass' : self.mass,
            'hair_color' : self.hair_color,
            'skin_color' : self.skin_color,
            'eye_color' : self.eye_color,
            'birth_year' : self.birth_year
        }

class CharacterData(BaseModel):
    id : int
    name : str
    height : int
    mass : int
    hair_color : str
    skin_color : str
    eye_color : str
    birth_year : int








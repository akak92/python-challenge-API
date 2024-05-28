from pydantic import BaseModel
from api import db
#
#   Pedro Díaz | 28-05-2023
#       models.py
#           clase Character:
#           Utilizada para interacciones ORM.
#           propiedad serialize() para retornar objetos en formato JSON
#
#           clase CharacterData:
#           Modelo simple para validaciones al crear Character
#           utilizando pydantic.
#

class Character(db.Model):
    __tablename__ = 'Character'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer,nullable=False)
    hair_color = db.Column(db.String(128), nullable=False)
    skin_color = db.Column(db.String(128), nullable=False)
    eye_color = db.Column(db.String(128), nullable=False)
    birth_year = db.Column(db.Integer,nullable=False)

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








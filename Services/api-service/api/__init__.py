from flask import Flask
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from api.models import Base, Character

#
#   Pedro Díaz | 28-05-2023
#       __init__.py   
#       funcion create_app():
#           Crea y retorna objeto app con definiciones necesarias 
#           para el correcto funcionamiento de la API.
#
#           Si falla su creación, logueamos.
#

def create_app():
    try:
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        app = Flask(__name__)

        engine = create_engine('sqlite:///characters.db', echo=True)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        

        app.Session = Session

        from api.controllers.Character import character_bp
        app.register_blueprint(character_bp, url_prefix='/character')

    except Exception as e:
        logging.info(f"Sucedió una excepción al crear la aplicación. {str(e)}")
    return app
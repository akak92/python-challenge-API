from flask import Flask
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models import Base, Character
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

#
#   Pedro Díaz | 28-05-2023
#       __init__.py   
#       funcion create_app():
#           Crea y retorna objeto app con definiciones necesarias 
#           para el correcto funcionamiento de la API.
#
#           Si falla su creación, logueamos.
#
#       swagger:
#           Implementamos flask-cors para permitir correcto funcionamiento.
#
#

def create_app():
    try:
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        app = Flask(__name__)
        CORS(app)

        engine = create_engine('sqlite:///characters.db', echo=True)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)

        app.Session = Session

        SWAGGER_URL = '/swagger'
        API_URL = '/static/swagger.json'
        SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
            SWAGGER_URL,
            API_URL,
            config = {
                'app_name' : 'Python Challenge - API'
            }
        )
    
        app.register_blueprint(SWAGGER_BLUEPRINT,url_prefix=SWAGGER_URL)
        from api.controllers.Character import character_bp
        app.register_blueprint(character_bp, url_prefix='/character')

    except Exception as e:
        logger.info(f"Sucedió una excepción al crear la aplicación. {str(e)}")
    return app
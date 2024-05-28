from flask import Flask
import logging
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import os

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

db = SQLAlchemy()

def create_app():
    try:
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        app = Flask(__name__)
        CORS(app)

        DB_NAME=os.getenv('DB_NAME', 'characters.db')

        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        from api.models import Character
        db.init_app(app)

        with app.app_context():
            db.create_all()

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
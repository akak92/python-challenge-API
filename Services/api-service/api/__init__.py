from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from api.models import Base, Character

def create_app():
    try:
        app = Flask(__name__)

        engine = create_engine('sqlite:///characters.db', echo=True)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        

        app.Session = Session

        from api.controllers.Character import character_bp
        app.register_blueprint(character_bp, url_prefix='/character')

    except Exception as e:
        pass
    return app
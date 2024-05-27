from flask import Blueprint, request, current_app
from api.models import Character, CharacterData

character_bp = Blueprint('character_bp', __name__)

@character_bp.route('/getAll', methods=['GET'])
def characters_get_all():
    try:
        session = current_app.Session()
        characters = session.query(Character).all()

        if characters is not []:
            message = "Characters obtenidos exitosamente."
            data = [character.serialize for character in characters]
            status = 200
        else:
            message = "No se han encontrado Characters."
            data = None
            status = 404

    except Exception as e:
        message = f"Ha ocurrido un error: {str(e)}"
        data = None
        status = 500
    finally:
        session.close()
    
    response = {
        'message' : message,
        'data' : data,
    }, status

    return response

@character_bp.route('/get/<int:id>', methods=['GET'])
def get(id):
    try:
        session = current_app.Session()
        character = session.query(Character).filter_by(id=id).first()

        if character is not None:
            data = character.serialize
            message = "Character obtenido exitosamente."
            status = 200
        else:
            data = None
            message = f"No se encontrado Character con id: {str(id)}"
            status = 404


    except Exception as e:
        data = None
        message = f"Ha ocurrido un error: {str(e)}"
        status = 500
    finally:
        session.close()

    response = {
        'message' : message,
        'data' : data
    }, status

    return response

@character_bp.route('/add', methods=['POST'])
def add():
    try:
        result = request.json
        new_character_data = CharacterData(**result)

        new_character = Character(**new_character_data.model_dump())

        session = current_app.Session()

        session.add(new_character)
        session.commit()

        message = "Character agregado exitosamente"
        status = 200
        data = new_character.serialize

    except Exception as e:
        message = f"Ha ocurrido un error {str(e)}"
        status = 500
        data = None
    finally:
        session.close()

    response = {
        'message' : message,
        'data' : data
    }, status

    return response
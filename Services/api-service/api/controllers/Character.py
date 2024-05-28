from flask import Blueprint, request
from api.models import Character, CharacterData
from api import db
#
#   Pedro Díaz | 28-05-2023
#   Character.py
#       Defino endpoints que cumplen ejercicio
#
#   [GET]   /getAll => Retorna todos los Characters.
#   [GET]   /get/{id} => Retorna Character filtrado por id proporcionado.
#   [POST]  /add => Agrego Character nuevo.
#   [DELETE] /delete/{id} => Elimino Character filtrado por id proporcionado.
#
#

character_bp = Blueprint('character_bp', __name__)

@character_bp.route('/getAll', methods=['GET'])
def characters_get_all():
    try:
        characters = Character.query.all()

        if characters != []:
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

    response = {
        'message' : message,
        'data' : data,
    }, status

    return response

@character_bp.route('/get/<int:id>', methods=['GET'])
def get_character(id):
    try:
        character = Character.query.filter_by(id=id).first()

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

    response = {
        'message' : message,
        'data' : data
    }, status

    return response

@character_bp.route('/add', methods=['POST'])
def add_character():
    try:
        result = request.json
        new_character_data = CharacterData(**result)
        new_character = Character(**new_character_data.model_dump())

        # Comprobación de existencia del character
        character = Character.query.filter_by(id=new_character.id).first()
        if character is None:
            db.session.add(new_character)
            db.session.commit()
            message = "Character agregado exitosamente"
            status = 200
            data = new_character.serialize
        else:
            message = "Character ya existe. No se puede agregar"
            status = 400
            data = None

    except Exception as e:
        message = f"Ha ocurrido un error. {str(e)}"
        status = 500
        data = None

    response = {
        'message': message,
        'data': data
    }, status

    return response

@character_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_character(id):
    try:
        character = Character.query.filter_by(id=id).first()

        if character is not None:
            Character.query.filter_by(id=id).delete()
            db.session.commit()
            message = f"Character con id: {str(id)} eliminado correctamente."
            status = 200
        else:
            message = f"Character con id: {str(id)} no existe."
            status = 400
        
    except Exception as e:
        message = f"Ha ocurrido un error. {str(e)}"
        status = 500

    response = {
        'message' : message
    }, status

    return response

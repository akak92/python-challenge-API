
#
#
#   Pedro Díaz | 28-05-2023
#       Pruebas unitarias para verificar el funcionamiento
#       de los endpoints de Character.
#



def test_getAll_characters(client):
    response = client.get('/getAll')
    assert response.status_code == 200

def test_get_character(client):
    character_id = 1
    response = client.get(f'/get/{character_id}')

    assert response.status_code == 200

def test_add_character(client):
    character_data = {
        "id": 1,
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY"
    }

    response = client.post('/add', json=character_data)

    assert response.status_code == 200

def test_delete_character(client):
    character_id = 1
    response = client.delete(f'/delete/{character_id}')

    assert response.status_code == 200

def test_get_invalid_character(client):

    invalid_character_id = 9999
    response = client.get(f'/get/{invalid_character_id}')

    assert response.status_code == 404

def test_add_existing_character(client):
    existing_character_data = {
        "id": 1,
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY"
    }

    response = client.post('/add', json=existing_character_data)
    assert response.status_code == 400

def test_delete_nonexistent_character(client):
    nonexistent_character_id = 9999
    response = client.delete(f'/delete/{nonexistent_character_id}')

    # Verificar que se recibe un código de estado 400 y el mensaje adecuado
    assert response.status_code == 400
from api import create_app
import os
#
#   Pedro Díaz | 28-05-2023
#
#       run.py:
#           Puerta de entrada de la aplicación.
#           Importamos create_app() y creamos objeto
#           Por default utilizamos puerto 5000 e IP local de host. (0.0.0.0)
#


app = create_app()

if __name__ == '__main__':
    API_HOST = os.getenv('API_HOST')
    API_PORT = os.getenv('API_PORT')
    app.run(host=API_HOST, port=API_PORT)
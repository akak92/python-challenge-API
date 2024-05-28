from api import create_app

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
    app.run(host='0.0.0.0', port=5000)
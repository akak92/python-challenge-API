# python-challenge-API

API que permite la realización de operaciones CRUD sobre una base de datos SQLite.

#### Herramientas / Frameworks

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

## Pre - requisitos

Tener instalados Docker & docker-compose. Para mayor información, visite [este enlace](https://docs.docker.com/manuals/).

Tener instalado Git. Puede descargarlo [aquí](https://git-scm.com/downloads)

## Instalación

Descargue el repositorio utilizando el siguiente comando:
```
git clone https://github.com/akak92/python-challenge-API.git
```

Diríjase al directorio del repositorio utilizando el comando `cd` y cambie el nombre del archivo `.env.example` a `.env`

#### En Windows:
```
ren .env.example .env
```
#### En Linux:
```
mv .env.example .env
```

#### Archivo .env

Aquí se encuentran alojadas variables de entorno que son utilizadas por la API para su inicialización.
```
API_HOST=0.0.0.0
API_PORT=5000
```
Por defecto, ya existen valores cargados para un correcto funcionamiento del aplicativo.

#### Inicializar API

Ejecute el siguiente comando para inicializar el contenedor:
```
docker-compose up --build --remove-orphans -d
```
El contenedor se inicializará en segundo plano, gracias al argumento `-d`. 
Recuerde que para ver los logs del contenedor puede utilizar el comando:
```
docker logs <NOMBRE_DEL_CONTENEDOR>
```
## Descripción

Se ha creado una API utilizando `Flask` para realizar operaciones `CRUD` (crear, leer, actualizar y borrar) sobre una entidad denominada Character (Personajes). 
Como método de persistencia se utiliza una base de datos SQLite, llamada `characters`.

Se ha utilizado `Docker-Compose` como medio de virtualización de la API (servicio api), facilitando así su mantenimiento y futura escalabilidad, mejorando de esta manera el ciclo de vida del aplicativo.

Todos los endpoints cuentan con el prefijo: `/character`
Los endpoints disponibles en la API se detallan a continuación:

`/getAll [GET]` : Obtiene todos los Characters de la tabla Character.

`/get/{id} [GET]` : Proporcionando el id, se obtiene el Character solicitado.

`/add [POST]` : Permite agregar nuevos Character a la base de datos SQLite.

`/delete/{id} [DELETE]` : Elimina el Character asociado al id proporcionado.


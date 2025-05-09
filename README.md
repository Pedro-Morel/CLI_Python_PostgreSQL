# crud_postgres

CRUD en Python utilizando **PostgreSQL**, con conexión a la base de datos mediante **psycopg2** y gestión de variables de entorno usando **python-dotenv**.

##  Características

- CRUD completo sobre una tabla `persona`.
- Conexión segura a PostgreSQL mediante variables de entorno.
- Uso de `psycopg2` para interacción con la base de datos.
- Estructura modular y clara para fácil mantenimiento, reutilización y escalabilidad.
- Operación mediante CLI

## Requisitos

- Python 3.8 o superior
- PostgreSQL instalado y configurado
- Paquetes necesarios:
  - `psycopg2`
  - `python-dotenv`
  - `os`

## Configuración

Cree un archivo .env en la raíz del proyecto basandose en el archivo .env.template proporcionado. Este archivo debe contener las siguientes variables de entorno:

DB_HOST=localhost  
DB_PORT=5432  
DB_NAME=nombre_de_su_base  
DB_USER=su_usuario  
DB_PASSWORD=su_contraseña

## Para instalar las dependencias, utilice el siguiente comando:

pip install -r requirements.txt

## Para ejecutar el proyecto desde la línea de comandos, utilice el siguiente comando:

python -m crud_postgres.main

## Nota: Debe crear la base de datos personas y la tabla persona:

CREATE DATABASE personas;  

CREATE TABLE persona (  
  id SERIAL PRIMARY KEY,  
  nombre CHARACTER VARYING(100) NOT NULL,  
  apellido CHARACTER VARYING(100) NOT NULL,  
  email CHARACTER VARYING(100) UNIQUE NOT NULL
);

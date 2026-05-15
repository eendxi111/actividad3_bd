 # Actividad 3 - Automatización de Base de Datos con Python y MySQL

## Descripción

Este proyecto automatiza la creación y llenado de una base de datos MySQL utilizando Python, SQLAlchemy y Faker.

El código realiza las siguientes funciones:

- Se conecta automáticamente a MySQL usando variables almacenadas en un archivo `.env`
- Crea una tabla llamada `personas_eendxi`
- Genera 100000 registros falsos con Faker (nombre, apellido, teléfono, email, fecha de nacimiento y empresa)
- Inserta automáticamente los registros en la base de datos mediante SQLAlchemy
- Permite verificar la cantidad de registros insertados usando consultas SQL

---

## Dependencias utilizadas

El proyecto requiere las siguientes librerías:

- SQLAlchemy
- PyMySQL
- Faker
- python-dotenv

Para instalar todas las dependencias ejecutar:

```bash
pip install -r requirements.txt
```

---

## Configuración

Crear un archivo `.env` con:

```env
DB_USER=root
DB
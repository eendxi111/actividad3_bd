# Actividad 3 - Automatización de Base de Datos con Python, SQLAlchemy y Faker

## Descripción

Este proyecto automatiza la creación y llenado de una base de datos MySQL utilizando Python, SQLAlchemy y Faker.

El script realiza automáticamente las siguientes tareas:

- Conecta a MySQL utilizando variables almacenadas en un archivo `.env`
- Crea una tabla llamada `personas_eendxi` si no existe
- Genera 100000 registros falsos usando Faker
- Inserta los registros en la base de datos mediante SQLAlchemy

Los datos generados incluyen los siguientes atributos:

- nombre
- apellido
- telefono
- email
- ciudad
- direccion
- empresa
- fecha_nacimiento

---

## Dependencias

Instalar las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

Las librerías utilizadas son:

- SQLAlchemy
- PyMySQL
- Faker
- python-dotenv

---

## Configuración

Crear un archivo `.env` con la configuración de conexión:

```env
DB_USER=root
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=taller_python
```

---

## Ejecución

Comando exacto para ejecutar el script:

```bash
python main.py
```

---

## Resultado esperado

Al ejecutar el script:

1. Se crea automáticamente la tabla:

```text
personas_eendxi
```

2. Se insertan:

```text
100000 registros
```

3. Para verificar la inserción:

```sql
SELECT COUNT(*)
FROM personas_eendxi;
```

Resultado esperado:

```text
100000
```

---


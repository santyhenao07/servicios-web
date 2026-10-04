# Clase 7 - ORM con FastAPI y PostgreSQL

## Tema

En esta clase conectamos una API de FastAPI con PostgreSQL usando un ORM.

## ¿Qué es un ORM?

ORM significa **Object Relational Mapping**. Permite trabajar con una base de datos usando clases y objetos de Python.

- Una clase representa una tabla.
- Un atributo representa una columna.
- Un objeto representa un registro.
- SQLAlchemy es el ORM utilizado en este proyecto.

## Estructura del proyecto

```text
main.py              Inicio de FastAPI
database.py          Conexión y sesiones de PostgreSQL
models/              Modelos ORM que representan tablas
schemas/             Validación de datos con Pydantic
crud/                Operaciones de base de datos
api/                 Rutas o endpoints
requirements.txt     Dependencias
.env.example         Ejemplo de variables de entorno
```

## Función de cada carpeta

- `models/`: contiene las clases de SQLAlchemy.
- `schemas/`: valida los datos recibidos y enviados por la API.
- `crud/`: contiene las operaciones de crear, consultar, actualizar y eliminar.
- `api/`: contiene las rutas que puede consumir el usuario.
- `database.py`: configura la conexión y las sesiones de la base de datos.

## Configuración

Crear el archivo local de variables de entorno:

```bash
cp .env.example .env
```

Completar `.env` con los datos reales de PostgreSQL. Este archivo no debe subirse a Git.

Instalar dependencias y ejecutar la API:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

La documentación está disponible en:

```text
http://127.0.0.1:8000/docs
```

## Endpoints de estudiantes

| Método | Ruta | Función |
|---|---|---|
| GET | `/estudiantes` | Listar estudiantes |
| GET | `/estudiantes/{id}` | Consultar un estudiante |
| POST | `/estudiantes` | Crear un estudiante |
| PUT | `/estudiantes/{id}` | Reemplazar un estudiante |
| PATCH | `/estudiantes/{id}` | Actualizar parcialmente |
| DELETE | `/estudiantes/{id}` | Eliminar un estudiante |
| GET | `/health/db` | Verificar la conexión |

## Tarea: implementar mediciones

La base de datos ya contiene la tabla `public.mediciones`. No se debe crear otra tabla ni cambiar su estructura.

### Estructura de la tabla

| Columna | Tipo | Obligatoria | Descripción |
|---|---|---|---|
| `id` | integer | Sí | Identificador principal |
| `estudiante_id` | integer | Sí | Estudiante relacionado |
| `variable` | varchar(50) | Sí | Nombre de la medición |
| `valor` | numeric | Sí | Valor registrado |
| `unidad` | varchar(20) | Sí | Unidad del valor |
| `fecha_hora` | timestamp with time zone | Sí | Fecha y hora de la medición |

`estudiante_id` es una llave foránea que apunta a `estudiantes.id`. Para crear una medición se debe utilizar un estudiante existente.

### Orden de implementación

1. **Pydantic:** crear los schemas de entrada, actualización y respuesta.
2. **ORM:** crear en `models/` la clase que represente `mediciones` y su relación con `estudiantes`.
3. **CRUD:** crear en `crud/` las funciones para listar, consultar, crear, actualizar y eliminar.
4. **API:** crear en `api/` los endpoints que utilicen las funciones CRUD.
5. **Pruebas:** probar todas las operaciones desde Swagger en `/docs`.

La API debe permitir listar, consultar, crear, actualizar y eliminar mediciones.

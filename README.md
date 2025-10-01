# Backend FastAPI Portal de Ofertas

✨ **Proyecto:** API REST para gestionar empresas y ofertas
**Tecnologías:** FastAPI, Python, SQLAlchemy, PostgreSQL
**Estado:** CRUD básico funcionando, listo para integrar con frontend.

---

## Descripción

Este proyecto es un **backend en FastAPI** que permite gestionar empresas y ofertas para estudiantes.
Incluye:

* Endpoints CRUD para empresas y ofertas.
* Conexión a base de datos PostgreSQL.
* Validación de datos con Pydantic.
* Documentación automática con Swagger y Redoc.

---

## Instalación

1. Clona el repositorio:

```
git clone https://github.com/Carmencalvocano/backend-fastapi-ofertas.git
cd backend-fastapi-ofertas
```

2. Crea un entorno virtual (recomendado):

```
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Instala dependencias:

```
pip install -r requirements.txt
```

4. Configura la conexión a PostgreSQL en `database.py`:

```
SQLALCHEMY_DATABASE_URL = "postgresql://usuario:password@localhost:5432/ofertas_db"
```

5. Ejecuta la API:

```
uvicorn main:app --reload
```

6. Abre documentación:

* Swagger → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* Redoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Estructura del proyecto

```
backend-fastapi-ofertas/
 ┣ main.py          # API FastAPI + endpoints
 ┣ models.py        # Tablas SQLAlchemy
 ┣ schemas.py       # Schemas Pydantic
 ┣ crud.py          # Funciones CRUD
 ┣ database.py      # Conexión a PostgreSQL
 ┣ requirements.txt # Dependencias
```

---

## Cómo usar

* Crear empresas con `POST /empresas/`.
* Listar empresas con `GET /empresas/`.
* Crear ofertas con `POST /ofertas/`.
* Listar ofertas con `GET /ofertas/`.
* Documentación y pruebas automáticas en Swagger.

---

## Próximos pasos

* Relacionar empresas ↔ ofertas en las respuestas.
* Integración con frontend Next.js para mostrar datos reales.
* Autenticación de usuarios (login/registro).
* Deploy en Render/Railway para pruebas en producción.

---

## Autor

Carmen Calvo Cano – [Carmencalvocano](https://github.com/Carmencalvocano)

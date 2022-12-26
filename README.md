# FastAPI Project Base

## Development

```
cp .env.sample .env
uvicorn app.main:app --reload
```


### Pytest

```
poetry run pytest
```

If you are in poetry shell (venv activated),

```
pytest
```
## PostgreSQL Database

### Migration
#### Initial Migration

```
alembic init -t async migrations
```

#### Create Migration
```
alembic revision --autogenerate -m "sample revision message"
```

#### Apply Migration
```
alembic upgrade head
```



## Dependencies
Here is a short description of python packages used in the article (just to make a whole picture to save your time):

1. [Poetry](https://python-poetry.org) - is a tool for dependency management and packaging in Python. It allows you to
   declare the libraries your project depends on and it will manage (install/update) them for you;
2. [FastAPI](https://fastapi.tiangolo.com) - is a modern, fast (high-performance), web framework for building APIs with
   Python 3.6+ based on standard Python type hints;
3. [Pydantic](https://pydantic-docs.helpmanual.io) - Data validation and settings management using Python type hinting;
4. [SQLAlchemy](https://www.sqlalchemy.org) - SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that
   gives application developers the full power and flexibility of SQL;
5. [SQLModel](https://sqlmodel.tiangolo.com) - SQLModel is a library for interacting with SQL databases from Python
   code, with Python objects;
6. [Alembic](https://alembic.sqlalchemy.org/en/latest/) - Alembic is a lightweight database migration tool for usage
   with the SQLAlchemy Database Toolkit for Python.

## Docker
### Docker Image
```
docker build -t mall-service .
```
### Docker run

Prepare .env file (see .env.sample) then,
```
docker run -p 8000:8000 --env-file .env --net="host" mall-service
```
Please note that --net="host"  doest not work on MacOS!

## TODO
- Add cache (fastapi_cache)

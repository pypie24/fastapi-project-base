FROM python:3.9-alpine

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY requirements.txt /app/


# Project initialization:
RUN pip install -r requirements.txt

# Creating folders, and files for a project:
COPY . /app

CMD ["sh","-c","cd /app/ && alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]

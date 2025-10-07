FROM python:3.13-slim

LABEL maintainer="Jeremías jeremyakd@gmail.com" \
      version="1.0" \
      description="Todo Project API - Django + DRF"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

WORKDIR /app/todo_project

ARG DJANGO_SECRET_KEY
ARG DEBUG
ARG ALLOWED_HOSTS

ENV DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
ENV DEBUG=$DEBUG
ENV ALLOWED_HOSTS=$ALLOWED_HOSTS


RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "todo_project.wsgi:application", "--bind", "0.0.0.0:8000"]
